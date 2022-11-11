#Neste programa, terao varios poligonos na tela, com colisão.
#rotacao, movimento, botoes, redimencionamento da janela sao os objetivos

import pygame
import math

pygame.init()

class Entidade():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velx = 0
        self.vely = 0
        self.angulo = 0

class Poligono(Entidade):
    def __init__(self,cor,obj_Janela):#tinha listaPontos
        self.listaPontos = []
        self.cor = cor #[R,G,B]
        self.estadoCor = 1
        self.surface = obj_Janela

    def Clarear(self):
        if self.cor[0] <= 235:
            self.cor[0] += 20
            
        if self.cor[0] > 235:
            self.cor[0] = 255

        if self.cor[1] <= 235:
            self.cor[1] += 20

        if self.cor[1] > 235:
            self.cor[1] = 255

        if self.cor[2] <= 235:
            self.cor[2] += 20

        if self.cor[2] > 235:
            self.cor[2] = 255

    def Escurecer(self):
        if self.cor[0] >= 20:
            self.cor[0] -= 20
            
        if self.cor[0] < 20:
            self.cor[0] = 0

        if self.cor[1] >= 20:
            self.cor[1] -= 20

        if self.cor[1] < 20:
            self.cor[1] = 0

        if self.cor[2] >= 20:
            self.cor[2] -= 20

        if self.cor[2] < 20:
            self.cor[2] = 0

    def Colorindo(self):
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
        
        

    def Rotacionar(self,pontoRef,angulo):#em graus
        self.angulo = angulo
        angulo = math.radians(angulo)
        for ponto in range(len(self.listaPontos)):
            x = self.listaPontos[ponto][0] - pontoRef[0]
            y = self.listaPontos[ponto][1] - pontoRef[1]

            x1 = x * math.cos(angulo) + y * math.sin(angulo)#-
            y1 = x * math.sin(angulo) - y * math.cos(angulo)#+

            self.listaPontos[ponto][0] = x1 + pontoRef[0]
            self.listaPontos[ponto][1] = y1 + pontoRef[1]

    def DesenharPoligono(self):
        pygame.draw.polygon(self.surface, self.cor, self.listaPontos)

class Botao(Poligono):
    def __init__(self,ponto,largura,altura):#basicamente um retangulo
        pygame.mouse.get_pressed(num_buttons=3)
        pygame.mouse.get_pos()#(x,y)

    def click(self):
        if self.x <= pygame.mouse.get_pos()[0] <=self.x + self.largura:
            if self.y <= pygame.mouse.get_pos()[1] <=self.y + self.altura:
                self.Clarear()
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.Escurecer()
                    return True

class Janela():
    def __init__(self,largura,altura,titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.janela = None
        
    def IniciarJanela(self):
        self.janela = pygame.display.set_mode((self.largura,self.altura))
        pygame.display.set_caption(self.titulo)

    def FecharJanela(self):
        pygame.quit()

    def TelaCheia(self):
        pygame.display.toggle_fullscreen()

def main():
    sair = False
    clock = pygame.time.Clock()#opa
    largura, altura = 800, 600
    tela = Janela(largura,altura,"Programa 04 PyGame - Poligonos e Rotação")
    tela.IniciarJanela()
    a = Poligono([0,0,0],tela.janela)
    b = Poligono([255,0 ,0 ],tela.janela)
    c = Poligono([200,0,200],tela.janela)
    d = Poligono([200,0,200],tela.janela)
    e = Poligono([200,0,200],tela.janela)
    f = Poligono([200,0,200],tela.janela)
    g = Poligono([200,0,200],tela.janela)
    h = Poligono([200,0,200],tela.janela)
    poligonos = [a,b,c,d,e,f,g,h]
    
    #quantidadePoligonos = int(input("Quantidade de Poligono(s): "))
    #print("Escreva a lista de pontos do Poligono(s). Ex: [[x1,x1],[x2,y2],...,]")
    #listaPoligonos = [0]*quantidadePoligonos
    #i = 0
    #while i < quantidadePoligonos:
    #    print("Poligono ",i+1,": ",end = '')
    #    listaPoligonos[i] = list(input(''))
    #    print(listaPoligonos[i])
    #    i += 1
    b.listaPontos = [[300,200],[500,200],[500,400],[300,400]]
    a.listaPontos = [[0,0],[800,0],[800,600],[0,600]]
    quantidadePoligonos = 2
    print("OK")
    ang = 0
    while not sair:
        clock.tick(60)
        pygame.display.update()
        i = 0
        while i < quantidadePoligonos:
            #poligonos[i].listaPontos = listaPoligonos[i]
            poligonos[i].DesenharPoligono()
            i += 1

        #botando para rodar:
        b.Rotacionar([400,300],ang)
        b.Colorindo()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            pygame.display.toggle_fullscreen()
        if keys[pygame.K_RIGHT]:
            ang -= 1
        if keys[pygame.K_LEFT]:
            ang += 1
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tela.FecharJanela()
                sair = True

    return "Finalizado."
    
print(main())

    


        
