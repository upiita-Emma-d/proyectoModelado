import  pygame
from lista import lista_fun
pygame.init()
#imagenes cargadas
iniciobg=pygame.image.load("img/unidad.jpg")
#Colores
altura_de_pantalla=600
ancho_de_pantalla=600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
SR=218, 65, 103
green=0, 239, 0
block_color = (53,115,255)
bright_red=(255,0,0)
bright_green=0,255,0
pantalla = pygame.display.set_mode((ancho_de_pantalla,altura_de_pantalla))

clock = pygame.time.Clock()
def quitgame():
    pygame.quit()
def siguiente():
    lista_fun()
   

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(pantalla, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(pantalla, ic,(x,y,w,h))

    smallText = pygame.font.Font('font\Mate-Italic.ttf',30)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    pantalla.blit(textSurf, textRect)

def text_objects(text, font,col):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('font\Mate-Italic.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)



def menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        pantalla.blit(iniciobg,[-25,0])
        largeText = pygame.font.SysFont('font\Mate-Italic.ttf',50)
        TextSurf, TextRect = text_objects("Modelado y Simulacion ", largeText, white )
        TextRect.center = ((ancho_de_pantalla/2),(altura_de_pantalla/2))
        pantalla.blit(TextSurf, TextRect)
        button('Veamos !',100,500,100,50,green,bright_green,siguiente)
        button("Cerrar",400,500,100,50,red,bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)
    
