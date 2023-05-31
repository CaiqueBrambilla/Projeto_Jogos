import json
import pygame
import sys


# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Game Over")

# Carregando a fonte
fonte = pygame.font.Font(None, 36)

# Pontuações de exemplo (você pode substituir por suas próprias pontuações)
pontos = 0

x = True

with open('nome.txt', 'r') as arquivo:
        nome = arquivo.read() 

with open('pontos.txt', 'r') as arquivo:
        pontos = arquivo.read() 

def adicionar_jogador(): 
    jogador_atual = {
               'nome': str (nome),
               'pontos': int (pontos)
        }

    with open('ranking.json', 'r') as arquivo:
        ranking = json.load(arquivo)

    ranking.append(jogador_atual)

    with open('ranking.json', 'w') as arquivo:
        json.dump(ranking, arquivo)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if x == True:
            adicionar_jogador()
            x = False
 


    # Preenchendo a tela com a cor preta
    tela.fill(BLACK)

    with open('ranking.json', 'r') as arquivo:
            ranking = json.load(arquivo)

    # Renderizando o texto "Game Over"
    texto_gameover = fonte.render("Game Over", True, WHITE)
    posicao_texto = texto_gameover.get_rect(center=(largura_tela // 2, altura_tela // 2 - 50))
    tela.blit(texto_gameover, posicao_texto)

    ranking.sort(key=lambda jogador: int(jogador['pontos']), reverse=True)

    # Renderizando o ranking
    posicao_ranking_y = altura_tela // 2  # Posição inicial do ranking
    for i, (jogador) in enumerate(ranking):
        posicao = i+1
        texto_ranking = fonte.render(f"{posicao}. {jogador ['nome']}: {jogador ['pontos']}", True, WHITE)
        posicao_ranking = texto_ranking.get_rect(center=(largura_tela // 2, posicao_ranking_y))
        tela.blit(texto_ranking, posicao_ranking)
        posicao_ranking_y += 40

    pygame.display.flip()
