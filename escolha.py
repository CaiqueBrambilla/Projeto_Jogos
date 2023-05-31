import sys
import pygame
from pygame.locals import*
from botao import Button

pygame.init()

# Cria a surface 
size = (1200,600)
screen = pygame.display.set_mode(size)

imagem = pygame.image.load("fazenda.jpg")

jeramy = pygame.image.load("jeramy_grande.png")

hillary = pygame.image.load("hillary_grande.png")

fonte = pygame.font.Font('VT323-Regular.ttf', 50)

escolha_personagem = fonte.render("SELECIONE SEU PERSONAGEM", True, (255,0,100))

while True:
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posicaomouse = pygame.mouse.get_pos()

    screen.blit(imagem,(0,0))
    screen.blit(hillary,(690,65)) 
    screen.blit(jeramy,(420,70))
    screen.blit(escolha_personagem,(410,10))

    BOTAO_JERAMY = Button(image=None, pos=(505,280), text_input='Jeramy', font=fonte, base_color='BLACK', hovering_color='BROWN')
    
    BOTAO_HILLARY = Button(image=None, pos=(780,280), text_input='Hillary', font=fonte, base_color='BLACK', hovering_color='RED')

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
        