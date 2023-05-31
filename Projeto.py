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
pygame.display.set_caption("Rain of Cards")

with open ('escolha.txt', 'r') as arquivo:
    escolha = arquivo.read()



#Carrega a imagem de fundo
imagem = pygame.image.load("fazenda.jpg")

#martina = pygame.image.load("martina.png")

ze = pygame.image.load("jeramy.png")

tempestade = pygame.image.load("tempestade_def.png")
abrigo_tempestade = pygame.image.load("abrigo_tempestade_def.png")
furacao = pygame.image.load("furacao_def.png")
abrigo_furacao = pygame.image.load("abrigo_furacao_def.png")
terremoto = pygame.image.load("terremoto_def.png")
abrigo_terremoto = pygame.image.load("abrigo_terremoto_def.png")
tsunami = pygame.image.load("tsunami_def.png")
abrigo_tsunami = pygame.image.load("abirgo_tsunami_def.png")
hillary = pygame.image.load("hillary.png")

widith_carta = 101
hight_carta = 50

widith_ze = 128
hight_ze = 100

personagem = ze

class Abrigo:
    def __init__ (self, nome, imagem):
        self.nome = nome
        self.imagem = imagem 

tempestadeA = Abrigo("Tempestade", pygame.image.load("abrigo_tempestade_def.png"))
furacaoA = Abrigo("Turacao", pygame.image.load("abrigo_furacao_def.png"))
tsunamiA = Abrigo("Tsunami", pygame.image.load("abirgo_tsunami_def.png"))
terremotoA = Abrigo("Terremoto", pygame.image.load("abrigo_terremoto_def.png"))

class Desastre:
    def __init__ (self, nome, imagem):
        self.nome = nome
        self.imagem = imagem 

tempestadeD = Desastre("Tempestade", pygame.image.load("tempestade_def.png"))
furacaoD = Desastre("Turacao", pygame.image.load("furacao_def.png"))
tsunamiD = Desastre("Tsunami", pygame.image.load("tsunami_def.png"))
terremotoD = Desastre("Terremoto", pygame.image.load("terremoto_def.png"))

Abrigos = [tempestadeA,furacaoA,tsunamiA,terremotoA]

Desastres = [tempestadeD,furacaoD,tsunamiD,terremotoD]

    

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
velocidadePersonagem = [5, 5]

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
temporizador = 0

desastre_atual = Desastres[1]
abrigo_atual = Abrigos[2]

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
            temporizador = temporizador +1

            if temporizador >= 140:
                with open('pontos.txt', 'w') as arquivo:
                    arquivo.write(str (placar)) 
                import game_over

    relogio = font.render(str (temporizador), True, (0,0,0))
        
    if escolha == '0':
        personagem = ze
    if escolha == '1':
        personagem = hillary

    # Verifica se alguma tecla foi pressionada, e captura o evento
    pressed = pygame.key.get_pressed()

    #Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
    if pressed[pygame.K_LEFT]: posicaojogador[0] -= velocidadePersonagem[0]
    if pressed[pygame.K_RIGHT]: posicaojogador[0] += velocidadePersonagem[0]

    #blita a imagem de fundo na tela
    screen.blit(imagem, (0, 0))
    screen.blit(relogio,(500,50))


    # Desenha um circulo branco na tela

    # Aqui é setado a posição inicial da bola vermelha
    if criar == True:
        X_carta = randint(230,950)
        Y_carta = -50
        x = randint(0,3)

        abrigo_atual = Abrigos[x]
        criar = False

        
    # Velocidade de queda do círculo Vermelho
    Y_carta += 5

    # Valores da bola vermelha é atribuido 
    posicaoCarta = [X_carta,Y_carta]


    # Se o círculo vermelho ultapassar a  tela ela é reiniciada
    if Y_carta > 600:
        if(abrigo_atual.nome == desastre_atual.nome):
            placar -= 1
        criar = True

    if temporizador >= 20:
        Y_carta += 2
        velocidadePersonagem = [7,7]
    if temporizador >= 40:
        Y_carta += 2
        velocidadePersonagem = [8,8]
    if temporizador >= 60:
        Y_carta += 1
        velocidadePersonagem = [10,10]
    if temporizador >= 80:
        Y_carta += 1
        velocidadePersonagem = [10,10]
    if temporizador >= 100:
        Y_carta += 1
        velocidadePersonagem = [11,11]
    if temporizador >= 120:
        Y_carta += 1
        velocidadePersonagem = [11,11]
    
    
    if((posicaojogador[0] + hight_ze >= posicaoCarta[0] and posicaojogador[0] <= posicaoCarta[0] + hight_carta) and(posicaojogador[1] + 40 <= posicaoCarta[1] + widith_carta and posicaojogador[1] + widith_ze >= posicaoCarta[1])):

        if(abrigo_atual.nome == desastre_atual.nome):
            placar += 1
            
            x = randint(0,3)

            desastre_atual = Desastres[x]

            
        else:
            placar -= 1
        print(n_carta_abrigo)
        print(n_carta_desastre)
        criar = True
        
        

    # renderizando as fontes do placar na tela
    score1 = font.render('Placar: '+str(placar), True, (WHITE))
    screen.blit(score1, (600, 50))


    screen.blit(personagem,posicaojogador)
    screen.blit(abrigo_atual.imagem,posicaoCarta)
    screen.blit(desastre_atual.imagem,posi_desastre)


    
    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)
