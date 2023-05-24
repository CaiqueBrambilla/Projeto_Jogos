
import pygame

class Abrigo:
    def _init_ (self, nome, imagem):
        self.nome = nome
        self.imagem = imagem 

tempestade = Abrigo("tempestade", pygame.image.load("tempestade_def.png"))
