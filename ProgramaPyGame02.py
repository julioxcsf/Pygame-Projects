import pygame
import sys

pygame.init()
larguraJanela = 800
alturaJanela = 600

class Bola():
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.velocidadeX = 0
        self.velocidadeY = 0

    def cair(self,alturaDaJanela):
        pass

    def move(self, comprimentoDaJanela):
        self.posicao = self.pos.move(self.velocidadeX,self.velocidadeY)
        if self.pos.right > comprimentoDaJanela:
            self.pos.left = 0#?? nao sei o que é isso
            self.velocidadeX = int(-0.9 * self.velocidadeX)

    def colisao(self):
        if self.pos(larguraJanela-5):
            pass

def main():
    gameExit = False
    janela = pygame.display.set_mode((larguraJanela,alturaJanela))
    pygame.display.set_caption('Programa Pygame 01 - Bola Pulando')
    #fill(255,255,255)
    pygame.display.update()

    raioBolinha = 5
    bolinha = pygame.draw.circle(janela,(0,255,0,255),(int(larguraJanela/2),alturaJanela-15),raioBolinha)
    bola1 = Bola(bolinha, 0, 0)
    

    while not gameExit:
        #janela.fill(255,255,255)
        pygame.draw.rect(janela,(255,0,0),[0,alturaJanela-10,larguraJanela,10])#OK (chao)

        #janela.blit(chao, bola1.posicao, bola1.posicao)
        #pygame.draw.circle(janela,(0,255,0,255),(int(larguraJanela/2),alturaJanela-15),raioBolinha) #OK
        
        janela.blit(, bola1.y+bola1.velocidadeY)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

    
print(main())
