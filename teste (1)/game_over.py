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
ranking = [
    ("Jogador 1", 500),
    ("Jogador 2", 400),
    ("Jogador 3", 300),
    ("Jogador 4", 200),
    ("Jogador 5", 100)
]

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenchendo a tela com a cor preta
    tela.fill(BLACK)

    # Renderizando o texto "Game Over"
    texto_gameover = fonte.render("Game Over", True, WHITE)
    posicao_texto = texto_gameover.get_rect(center=(largura_tela // 2, altura_tela // 2 - 50))
    tela.blit(texto_gameover, posicao_texto)

    # Renderizando o ranking
    posicao_ranking_y = altura_tela // 2  # Posição inicial do ranking
    for i, (jogador, pontuacao) in enumerate(ranking):
        texto_ranking = fonte.render(f"{i+1}. {jogador}: {pontuacao}", True, WHITE)
        posicao_ranking = texto_ranking.get_rect(center=(largura_tela // 2, posicao_ranking_y))
        tela.blit(texto_ranking, posicao_ranking)
        posicao_ranking_y += 40

    pygame.display.flip()
