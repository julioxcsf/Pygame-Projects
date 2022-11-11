import pygame
import sys

pygame.init()

class GameObject():
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.height = height
        self.pos = image.get_rect().move(0, height)#isso é responsavel pela mudanca
        #da posicao da imagem na janela
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0

    def cair(self):
        self.height += 1
        if self.height == 480:
            self.height = 0

def IniciarJanela():
    screen = pygame.display.set_mode((640, 480))
    background = pygame.image.load('Pygame00-Background2.jpg').convert()
    player = pygame.image.load('Pygame00-Hero1.jpg')#.convert() !!!UÉ
    screen.blit(background, (0, 0))
    o = GameObject(player, 0, 3)
    pygame.display.update()                #and show it all
    clock = pygame.time.Clock()

    while True:
        screen.blit(background, o.pos, o.pos)
        screen.blit(o.image, o.pos)
        pygame.display.update()
        o = GameObject(player, o.height, 3)
        o.cair()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()#nao ajudou
                
    return 0
                

print(IniciarJanela())
