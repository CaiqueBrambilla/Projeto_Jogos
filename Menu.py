import pygame
from Instrução import instrucoes

pygame.init()
resolucao = (1200, 600)
screen = pygame.display.set_mode(resolucao)

pygame.display.set_caption("Menu")
font = pygame.font.Font('VT323-Regular.ttf', 55)
font2 = pygame.font.Font('VT323-Regular.ttf', 120)

#Cria botão para opção de menu
play_button = pygame.Rect(resolucao[0]/2-100, resolucao[1]/2-100, 200, 50)
play_text = font.render("Jogar", True, (0, 0, 0))

instruction_button = pygame.Rect((resolucao[0]/2-100, resolucao[1]/2, 270, 50))
instruction_text = font.render("Instrução", True, (0, 0, 0))


#imagem de fundo
background_image = pygame.image.load("fazenda.jpg").convert()
story1 = font2.render("Rain of Cards", True, (0,0,0))

#Desenha elementos no menu da tela


#Música de fundo
sound = pygame.mixer.music.load("BoxCat Games - Victory.mp3")
pygame.mixer.music.play(-1)

'''sound = pygame.mixer.Sound("BoxCat Games - CPU Talk.mp3")
sound.play()
sound.set_volume(0.5)'''
som_ligado = True
botao_som = pygame.Rect(550, 370, 50, 50)

while True:
    # Background
    screen.blit(background_image, [0, 0])
    
    # Botoes
    play_button = pygame.draw.rect(screen,(0,255,0),play_button,0,10)
    instruction_button = pygame.draw.rect(screen,(0,255,0),instruction_button,0,10)
    screen.blit(play_text, (resolucao[0]/2-75, resolucao[1]/2-100))
    screen.blit(instruction_text, (resolucao[0]/2+-75, resolucao[1]/2))
    screen.blit(story1,(330,10))

    


     #Botão de som 1
    botao_som_img = pygame.image.load("botao-som.png").convert_alpha()
    botao_som_img = pygame.transform.scale(botao_som_img, (50, 50))
    
    
    # Botao som
    screen.blit(botao_som_img, botao_som)   
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pos = pygame.mouse.get_pos()

        # botão do som 2
        if pos[0] >= 200 and pos[0] <= 550+50 and pos[1] >= 370 and pos[1] <= 500:
                if som_ligado == True:
                    botao_som_img = botao_som
                elif som_ligado == False:   
                    botao_som = botao_som
                if event.type == pygame.MOUSEBUTTONDOWN:   
                    if som_ligado == True:
                        botao_som_img = botao_som
                        pygame.mixer.music.stop() 
                        som_ligado = False
                    elif som_ligado == False:   
                        botao_som_img = botao_som_img   
                        pygame.mixer.music.play() 
                        som_ligado = True 
        else:
                if som_ligado == True:
                    icone_som = botao_som_img
                elif som_ligado == False:   
                    icone_som = botao_som_img
       
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Jogar
            if pos[0] >= 500 and pos[0]<= 700 and pos[1]>170 and pos[1]<=250:
                print("play")
                import apelido

            # Instruçoes
            if pos[0] >= 500 and pos[0]<= 765 and pos[1]>=300 and pos[1]<=340:
                print('instrução')
                instrucoes()  
            
    pygame.display.update()
