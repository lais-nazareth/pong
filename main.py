from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

gol = False

def inicial(barra,barra2,bola):
    barra.set_position(0, (janela.height - barra.height) / 2)
    barra2.set_position(janela.width - barra2.width,(janela.height - barra2.height) / 2)
    bola.set_position(janela.width / 2, janela.height/2)

# Configuração de Janela

largura = 900
altura = 600

janela = Window(largura, altura)

janela.set_title("Dr Pong")

# Configuração de Cenário
cenario = GameImage("Images\house.png")

# Configurando bola (60x60)
bola = GameImage("Images\Foreman-dr-eric-foreman-2392800-1600-1200-modified_optimized.png")

velx = 0.8
vely = 0.2
vela = 0

bola.x = (janela.width/2) - (bola.width/2)
bola.y = (janela.height/2) - (bola.height/2)

# Configuração barra 1
barra = GameImage("Images\\barra.jpg")

teclado = Window.get_keyboard()

barra.y = (janela.height/2) - (barra.height/2)


# Configuração barra 2
barra2 = GameImage("Images\\barra2.jpg")

teclado = Window.get_keyboard()

barra2.x = janela.width - 20
barra2.y = (janela.height/2) - (barra.height/2)

# Pontos
pontos1 = 0
pontos2 = 0

# Game Loop
while True:
    cenario.draw()
    janela.draw_text(str(pontos1), 40, 40, 100, color=(0, 0, 0), font_name="Arial", bold=True)
    janela.draw_text(str(pontos2), 820, 40, 100, color=(0, 0, 0), font_name="Arial", bold=True)
    bola.draw()
    barra.draw()
    barra2.draw()


    # Movimento Vertical
    bola.y += vely
    if int(bola.y) == janela.height - 60:
        vela += 0.05
        vely = -0.2 -vela
    if int(bola.y) == 0:
        vela += 0.05
        vely = 0.2 + vela

    # Moviemnto Horizontal
    bola.x += velx

    # Movimento de Barra com Input
    if teclado.key_pressed("w") and int(barra.y) != 0:
        barra.y -= 0.5
    elif teclado.key_pressed("s") and int(barra.y) != (janela.height-barra.height):
        barra.y += 0.5

    # movendo a Barra Automaticamente
    if barra2.y + barra2.height / 2 < bola.y + bola.height / 2 and barra2.y <= janela.height - barra2.height:
        barra2.y += min(0.5, bola.y - (barra2.y + barra2.height / 2))
    elif barra2.y + barra2.height / 2 > bola.y + bola.height / 2 and barra2.y >= 0:
        barra2.y -= min(0.5, (barra2.y + barra2.height / 2) - bola.y)

    # Adicionando limites para evitar que a barra 2 saia da tela
    if barra2.y < 0:
        barra2.y = 0
    elif barra2.y > janela.height - barra2.height:
        barra2.y = janela.height - barra2.height

    # Colisão Barra 1
    # Bola
    if bola.collided(barra) and teclado.key_pressed("w"):
        velx = 0.8
        vely = -0.2 -vela

    elif bola.collided(barra) and teclado.key_pressed("s"):
        velx = 0.8
        vely = 0.2 +vela
    elif bola.collided(barra):
        velx = 0.8

    # Colisão Barra 2
    # Bola
    if bola.collided(barra2) and teclado.key_pressed("UP"):
        velx = -0.8
        vely = -0.2 -vela
    elif bola.collided(barra2) and teclado.key_pressed("DOWN"):
        velx = -0.8
        vely = 0.2 + vela
    elif bola.collided(barra2):
        velx = -0.8

    # Sistema de Pontos
    if bola.x <= 1:
        pontos1 += 1
        vely = 0
        velx = 0
        gol = True
        inicial(barra, barra2, bola)

    if bola.x >= janela.width - bola.width:
        pontos2 += 1
        vely = 0
        velx = 0
        gol = True
        inicial(barra, barra2, bola)

    if gol:
        if (teclado.key_pressed('space')):
            bola.set_position(janela.width / 2, janela.height / 2)
            vely = 0.8
            velx = 0.2

    janela.update()
