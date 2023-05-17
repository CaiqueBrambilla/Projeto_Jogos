#----------------PARTE 1-------------------------------------

# Importa as bibliotecas utilizadas
import sys, pygame
from pygame.locals import *
from random import *

# Inicializa a biblioteca pygame
pygame.init()

# Cria a surface 
size = (1200,600)
screen = pygame.display.set_mode(size)

# Define um titulo para a janela
pygame.display.set_caption("Papa Bolinhas")

#Carrega a imagem de fundo
imagem = pygame.image.load("background.png")

#martina = pygame.image.load("martina.png")

ze = pygame.image.load("zezao.png")

tempestade = pygame.image.load("tempestade_def.png")
abrigo_tempestade = pygame.image.load("abrigo_tempestade_def.png")
furacao = pygame.image.load("furacao_def.png")
abrigo_furacao = pygame.image.load("abrigo_furacao_def.png")
terremoto = pygame.image.load("terremoto_def.png")
abrigo_terremoto = pygame.image.load("abrigo_terremoto_def.png")
tsunami = pygame.image.load("tsunami_def.png")
abrigo_tsunami = pygame.image.load("abirgo_tsunami_def.png")

widith_carta = 101
hight_carta = 50

widith_ze = 128
hight_ze = 100


# Define as cores em RGB
BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Declarando a fonte do placar e variável contadora
font = pygame.font.SysFont('sans',40)
placar = 0

# Declara o vetor que controla a posicao X e Y do circulo 
posicaojogador = [600, 400]

# Armazena num vetor a Velocidade de movimentacao do circulo 
velocidadePapaBolinhas = [5, 5]

# Variável para iniciar a posição do círculo vermelho
criar = True

# Variáveis de posição do círculo vermelho
X_vermelho = 0
Y_vermelho = 0

# Variável para contagem de tempo, utilizado para controlar a velocidade de quadros (de atualizações da tela)
clock = pygame.time.Clock()

#criando objeto Clock
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo
temporizador = 60

desastre_atual = furacao
abrigo_atual = abrigo_furacao

n_carta_abrigo = 0
n_carta_desastre = 0

posi_desastre = (10,10)
#----------------PARTE 2-------------------------------------

# Loop principal do jogo
while True:
    
    # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #capturando evendo de relogio a cada 1 segundo e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador = temporizador -1

    #finalizando o jogo
    if temporizador == 0:
        # desenhando um frame ocupando e escondendo toda a tela do usuário
        break

    # Verifica se alguma tecla foi pressionada, e captura o evento
    pressed = pygame.key.get_pressed()

    #Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
    if pressed[pygame.K_LEFT]: posicaojogador[0] -= velocidadePapaBolinhas[0]
    if pressed[pygame.K_RIGHT]: posicaojogador[0] += velocidadePapaBolinhas[0]

    #blita a imagem de fundo na tela
    screen.blit(imagem, (0, 0))

    # Desenha um circulo branco na tela

    # Aqui é setado a posição inicial da bola vermelha
    if criar == True:
        X_vermelho = randint(40,760)
        Y_vermelho = -50
        num_carta = randint(0,3)

        if num_carta == 0:
            abrigo_atual = abrigo_furacao
            n_carta_abrigo = 0
        if num_carta == 1:
           abrigo_atual = abrigo_tempestade
           n_carta_abrigo = 1
        if num_carta == 2:
            abrigo_atual = abrigo_tsunami
            n_carta_abrigo = 2
        if num_carta == 3:
           abrigo_atual = abrigo_terremoto
           n_carta_abrigo = 3
        criar = False

        
    # Velocidade de queda do círculo Vermelho
    Y_vermelho += 5

    # Valores da bola vermelha é atribuido 
    posicaoBolasVermelhas = [X_vermelho,Y_vermelho]


    # Se o círculo vermelho ultapassar a  tela ela é reiniciada
    if Y_vermelho > 600:
        criar = True

    # Se o papa bolinhas encostar no círculo vermelho o círculo vermelho é reiniciado
    # CB: Círculo Branco    CV: Círculo Vermelho 
    
    
    if((posicaojogador[0] + hight_ze >= posicaoBolasVermelhas[0] and posicaojogador[0] <= posicaoBolasVermelhas[0] + hight_carta) and(posicaojogador[1] + 40 <= posicaoBolasVermelhas[1] + widith_carta and posicaojogador[1] + widith_ze >= posicaoBolasVermelhas[1])):

        if(n_carta_abrigo == n_carta_desastre):
            placar += 1
            
            x = randint(0,3)

            if x == 0:
                desastre_atual = furacao
                n_carta_desastre = 0
            if x == 1:
                desastre_atual = tempestade
            n_carta_desastre = 1
            if x == 2:
                desastre_atual = tsunami
                n_carta_desastre = 2
            if x == 3:
                desatre_atual = terremoto
                n_carta_desastre = 3
            
        else:
            placar -= 1
        print(n_carta_abrigo)
        print(n_carta_desastre)
        criar = True
        
        

    # renderizando as fontes do placar na tela
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, (600, 50))


    screen.blit(ze,posicaojogador)
    screen.blit(abrigo_atual,posicaoBolasVermelhas)
    screen.blit(desastre_atual,posi_desastre)


    
    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)
