import pygame

pygame.init()

class Retangulo():
    def __init__(self,cor,x_TopEsquerdo,y_TopEsquerdo,largura,altura):
        self.cor = cor #RGB(255,255,255)
        self.x = x_TopEsquerdo
        self.y = y_TopEsquerdo
        self.largura = largura
        self.altura = altura

    def moveHorizontal(self):
        self.x += 1

    def moveVertical(self):
        self.t -= 1
        
class Janela():
    def __init__(self, titulo, largura = 800, altura = 600):#deveria ter cor, mas o fill nao funciona
        self.largura = largura
        self.altura = altura
        #self.cor = (255,255,255)
        self.titulo = titulo
        

def colisaoHorizontal(limiteLeft,limiteRight,x,largura):
    if x == limiteLeft:
        return True
    elif x+largura == limiteRight:
        return True
    else:
        return False

def limiteVertical(limiteUp,limiteDown,y,altura):
    if y == limiteUp:
        return True
    elif y+altura == limiteDown:
        return True
    else:
        return False

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
    janela = Janela("Programa 01 PyGame - Retangulo")
    retangulo = Retangulo((255,255,255),350,250,100,100)
    while not gameExit:
        DesenharRetangulo(IniciarJanela(janela),retangulo)
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    return "OK"
    
print(main())
