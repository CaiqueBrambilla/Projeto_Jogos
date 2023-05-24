import sys
import pygame
from pygame.locals import*
from botao import Button

pygame.init()

# Cria a surface 
size = (1200,600)
screen = pygame.display.set_mode(size)

imagem = pygame.image.load("background.png")

jeramy = pygame.image.load("jeramy.png")

hillary = pygame.image.load("hillary.png")

fonte = pygame.font.Font('Pangolin-Regular.ttf', 30)

while True:
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posicaomouse = pygame.mouse.get_pos()

    screen.blit(imagem,(0,0))
    screen.blit(hillary,(700,300)) 
    screen.blit(jeramy,(600,300))

    BOTAO_JERAMY = Button(image=None, pos=(600,400), text_input='Jeramy', font=fonte, base_color='BLACK', hovering_color='GREEN')
    
    BOTAO_HILLARY = Button(image=None, pos=(700,400), text_input='Hillary', font=fonte, base_color='BLACK', hovering_color='GREEN')

    for button in [BOTAO_JERAMY, BOTAO_HILLARY]:
         button.changeColor(posicaomouse)
         button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BOTAO_JERAMY.checkForInput(posicaomouse):
                with open('escolha.txt', 'w') as arquivo:
                        arquivo.write('0')
                import Projeto
            if BOTAO_HILLARY.checkForInput(posicaomouse):
                with open('escolha.txt', 'w') as arquivo:
                        arquivo.write('1')
                import Projeto
    pygame.display.update()
        