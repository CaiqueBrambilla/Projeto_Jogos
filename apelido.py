import sys
import pygame
from pygame.locals import*
from botao import Button

pygame.init()

# Cria a surface 
size = (1200,600)
screen = pygame.display.set_mode(size)

imagem = pygame.image.load("fazenda.jpg")

fonte = pygame.font.Font('VT323-Regular.ttf', 40)

nome = ''

texto = fonte.render("DIGITE O NOME DE COMO QUER SER CHAMADO", True, (255,0,100))

while True:
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:                 
                nome = nome[:-1]
            else:
                 nome += event.unicode
             
    posicaomouse = pygame.mouse.get_pos()

    nome2 = fonte.render(nome, True, (0,0,0))

    screen.blit(imagem,(0,0))

    screen.blit(nome2,(530,200))

    screen.blit(texto,(330,100))

    BOTAO_CONFIRMA = Button(image=None, pos=(600,300), text_input='CONFIRMAR', font=fonte, base_color='BLACK', hovering_color='RED')
    
    for button in [BOTAO_CONFIRMA]:
         button.changeColor(posicaomouse)
         button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BOTAO_CONFIRMA.checkForInput(posicaomouse):
                 with open('nome.txt', 'w') as arquivo:
                    arquivo.write(nome) 
                 import escolha
    pygame.display.update()
        