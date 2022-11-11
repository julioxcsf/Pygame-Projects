# ======================================================================================
# Esse é igual ao ProgramaPygame01 com tentativa de mover o retangulo e testar a colisao
# ======================================================================================

import pygame
import os #para limpar saida

pygame.init()

class Retangulo(): # nesse programa, ainda se diferencia retangulo de outras
                   # entidades que aparecerao na tela.
                   
    def __init__(self,cor,x_TopEsquerdo,y_TopEsquerdo,largura,altura):
        self.cor = cor #RGB(255,255,255)
        self.estadoCor = 1
        self.x = x_TopEsquerdo
        self.y = y_TopEsquerdo
        self.largura = largura
        self.altura = altura
        self.velX = 0
        self.velY = 0

    def colorindo(self):
        r=self.cor[0]
        g=self.cor[1]
        b=self.cor[2]
        if r+g!=255 and g+b!=255 and r+b!=255:
            r,g,b = 255,0,0
            
        if self.estadoCor==1:
            r -= 1
            g += 1
            if r <= 0:
                self.estadoCor = 2
                
        elif self.estadoCor == 2:
            g -= 1
            b += 1
            if g<= 0:
                self.estadoCor = 3
        else:
            b -= 1
            r += 1
            if b <= 0 :
                self.estadoCor = 1
                
        self.cor = (r,g,b)

    def moveHorizontal(self):
        self.x += self.velX

    def moveVertical(self):
        self.y += self.velY

    def Move(self, up=False, down=False, left=False, right=False):
        if right:
            self.velX += 1
            if self.velX > 5:
                self.velX = 5
        if left:
            self.velX -= 1
            if self.velX < -5:
                self.velX = -5
            
        if down:
            self.velY += 1
            if self.velY > 5:
                self.velY = 5
        if up:
            self.velY -= 1
            if self.velY < -5:
                self.velY = -5
            
        print(self.velX,self.velY)
                
        self.moveHorizontal()
        self.moveVertical()


class Janela():
    def __init__(self, titulo, largura = 800, altura = 600):#deveria ter cor, mas o fill nao funciona
        self.largura = largura
        self.altura = altura
        #self.cor = (255,255,255)
        self.titulo = titulo
        #self.janela = pygame.display.set_mode((self.largura, self.altura))
        #pygame.display.set_caption(self.titulo)



def ColisaoHorizontal(limiteLeft,limiteRight,obj):
    if obj.x <= limiteLeft:
        return True
    elif obj.x + obj.largura >= limiteRight:
        return True
    else:
        return False

def ColisaoVertical(limiteUp,limiteDown,obj):
    if obj.y <= limiteUp:
        return True
    elif obj.y + obj.altura >= limiteDown:
        return True
    else:
        return False

def TeveColisao(limiteUp,limiteDown,limiteLeft,limiteRight,obj):
    if ColisaoHorizontal(limiteLeft,limiteRight,obj):
        obj.velX = -1 * obj.velX
    if ColisaoVertical(limiteUp,limiteDown,obj):
        obj.velY = -1 * obj.velY


def DesenharRetangulo(surface,obj_Retangulo):
    pygame.draw.rect(surface,obj_Retangulo.cor,\
    [obj_Retangulo.x,obj_Retangulo.y,obj_Retangulo.largura,obj_Retangulo.altura])

def IniciarJanela(obj_Janela):
    janelaW = pygame.display.set_mode((obj_Janela.largura, obj_Janela.altura))
    pygame.display.set_caption(obj_Janela.titulo)
    return janelaW
    
def main():
    gameExit = False
    clock = pygame.time.Clock()
    janela = Janela("Programa 03 PyGame - Retangulo com Colisão")
    retangulo = Retangulo((255,255,255),350,250,100,100)
    while not gameExit:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            retangulo.Move(up=True)
        if keys[pygame.K_DOWN]:
            retangulo.Move(down=True)
        if keys[pygame.K_LEFT]:
            retangulo.Move(left=True)
        if keys[pygame.K_RIGHT]:
            retangulo.Move(right=True)
        retangulo.Move()
        DesenharRetangulo(IniciarJanela(janela),retangulo)
        clock.tick(60)
        pygame.display.update()

        TeveColisao(0,600,0,800,retangulo)

        retangulo.moveHorizontal()
        retangulo.moveVertical()
            
        retangulo.colorindo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

print(main())
