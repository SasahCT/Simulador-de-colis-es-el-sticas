import pygame
import random
import math

class Bola:
    def __init__(self, x, y, raio, vx, vy):
        self.x = x
        self.y = y
        self.raio = raio
        self.vx = vx
        self.vy = vy


    def mover(self, width, height):
        
        self.x += self.vx
        self.y += self.vy

        #VERIFICAÇÕES PARA AS COLISÕES COM OS LIMITES DA JANELA 
        #SEMPRE QUE A BOLINHA BATE NA BORDA, ELA INVERTE DE DIREÇÃO!
        if self.x - self.raio < 0 or self.x + self.raio > width:
            self.vx *= -1
        if self.y - self.raio < 0 or self.y + self.raio > height:
            self.vy *= -1

def colisao(b1, b2):

    d = math.sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2)
    if d < (b1.raio + b2.raio):
        return True #HOUVE UMA COLISÃO
    return False #NÃO HOUVE UMA COLISÃO

def ajuste(b1, b2):
    
    b1.vx, b2.vx = b2.vx, b1.vx
    b1.vy, b2.vy = b2.vy, b1.vy

    overlap = 0.5 * (b1.raio + b2.raio - math.sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2))
    angulo = math.atan2(b2.y - b1.y, b2.x - b1.x)
    b1.x -= overlap * math.cos(angulo)
    b1.y -= overlap * math.sin(angulo)
    b2.x += overlap * math.cos(angulo)
    b2.y += overlap * math.sin(angulo)

qnt = 15  # QUANTIDADE DE BOLINHAS      
lista = [] # LISTA DAS BOLINHAS

# PREENCHENDO A LISTA COM AS BOLINHAS, E ESTAS COM SEUS RESPECTIVOS DADOS
for i in range(qnt):
    # GARANTE QUE NENHUMA DELAS TENHA VELOCIDADE NULA 
    vx = random.randrange(-5, 6) or 1
    vy = random.randrange(-5, 6) or 1
    lista.append(Bola(random.randrange(50, 721), random.randrange(50, 481), 30, vx, vy))

# CRIAÇÃO DA JANELA
White = (255, 255, 255)
width, height = 720, 480
Display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
run = True 

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Display.fill(White) # DEIXA A TELA EM BRANCO ANTES DA PRÓXIMA IMAGEM

    for bola in lista:
        bola.mover(width, height) # ATUALIZA AS POSIÇÕES DAS BOLINHAS
        pygame.draw.circle(Display, (0, 0, 0), (int(bola.x), int(bola.y)), bola.raio) # DESENHA AS BOLINHAS APÓS A ATUALIZAÇÃO DAS POSIÇÕES
    
    # VERIFICA SE HOUVE COLISÕES
    for i in range(qnt):
        for j in range(i + 1, qnt):
            if colisao(lista[i], lista[j]):
                #SE SIM, AJUSTA A VELOCIDADE E A POSIÇÃO
                ajuste(lista[i], lista[j])
    
    pygame.display.update()
pygame.quit()

