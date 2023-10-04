import random

import pygame
from pygame.locals import *
from sys import exit

from Jogador import Player
from Jogo import Game

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Love Letter")

jogo = Game()

maquina = Player()
player1 = Player()

maquina.add_card(jogo.draw_card())
player1.add_card(jogo.draw_card())

font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            quantidade_cartas = len(player1.cartas)
            espaco_usado = quantidade_cartas*51
            inicio = (640 - espaco_usado)//2
            fim = 640 - inicio

            if y >= 390 and inicio < x < fim:
                indice = (x - inicio) // 50
                player1.use_card(indice)

                # Turno da maquina
                maquina.add_card(jogo.draw_card())
                while len(maquina.cartas) > 1:
                    try:
                        maquina.use_card(random.randrange(0, len(maquina.cartas)))
                    except:
                        continue


    screen.fill((255, 255, 255))

    if len(player1.cartas) == 1:
        player1.add_card(jogo.draw_card())

    # Desenha quantas cartas faltam
    pygame.draw.rect(screen, (94, 33, 41), Rect((295, 200), (50, 80)))
    text = font.render(str(len(jogo.cartas)), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (320, 240)
    screen.blit(text, textRect)

    # Desenha a mão da máquina
    maquina_x = 320 - len(maquina.cartas)*25
    maquina_y = 10
    for card in maquina.cartas:
        pygame.draw.rect(screen, (94, 33, 41), Rect((maquina_x, maquina_y), (50, 80)))
        maquina_x += 51

    # Coloca as cartas na mesa
    maquina_x = 320 - len(maquina.mesa) * 25
    maquina_y = 110
    for card in maquina.mesa:
        pygame.draw.rect(screen, (94, 33, 41), Rect((maquina_x, maquina_y), (50, 80)))
        text = font.render(str(card.valor), True, green, blue)
        textRect = text.get_rect()
        textRect.center = (maquina_x + 25, maquina_y + 40)
        screen.blit(text, textRect)
        maquina_x += 51

    # Desenha a mão do jogador, com o valor das cartas
    jogador_x = 320 - len(player1.cartas)*25
    jogador_y = 390
    for card in player1.cartas:
        pygame.draw.rect(screen, (94, 33, 41), Rect((jogador_x, jogador_y), (50, 80)))
        text = font.render(str(card.valor), True, green, blue)
        textRect = text.get_rect()
        textRect.center = (jogador_x+25, jogador_y+40)
        screen.blit(text, textRect)
        jogador_x += 51

    # Coloca as cartas na mesa
    jogador_x = 320 - len(player1.mesa) * 25
    jogador_y = 300
    for card in player1.mesa:
        pygame.draw.rect(screen, (94, 33, 41), Rect((jogador_x, jogador_y), (50, 80)))
        text = font.render(str(card.valor), True, green, blue)
        textRect = text.get_rect()
        textRect.center = (jogador_x + 25, jogador_y + 40)
        screen.blit(text, textRect)
        jogador_x += 51

    pygame.display.update()