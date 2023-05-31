import pygame

pygame.init()

# Defina as dimensões da tela
largura = 1200
altura = 600
tela = pygame.display.set_mode((largura, altura))


def mostrar_instrucoes():
    font = pygame.font.SysFont(None, 30)
    instrucoes = [
        "Instruções:",
        "",
        "Bem vindo ao jogo!.",
        "Use as setas para mover",
        "Pressione a barra de espaço para atirar",
        "",
        "Pressione ESC para voltar ao menu principal"
    ]

#imagem do teclado
def instrucoes():
    instucao_image = pygame.image.load("instrucao.png").convert_alpha()
    
    fonte = pygame.font.Font('VT323-Regular.ttf', 70)

    titulo = fonte.render("INSTRUÇÕES", True, (255,0,100))

    # Desenhe as instruções na tela
    background_image = pygame.image.load("fazenda.jpg").convert()
    tela.blit(background_image, [0, 0])
    tela.blit(instucao_image, (100,100))
    tela.blit(titulo,(500,10))

    

    # Aguarde o usuário fechar a janela
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # Volte para a tela do menu ou execute a ação desejada
                    print("Voltando para o menu...")
                    return

        pygame.display.update()
