import random

from Cartas import *


class Game:

    def __init__(self):
        self.cartas = [
            Spy(),
            Spy(),
            Guard(),
            Guard(),
            Guard(),
            Guard(),
            Guard(),
            Guard(),
            Priest(),
            Priest(),
            Baron(),
            Baron(),
            Handmaid(),
            Handmaid(),
            Prince(),
            Prince(),
            Chancellor(),
            Chancellor(),
            King(),
            Countess(),
            Princess()
        ]

        self.carta_fora = self.cartas.pop(random.randint(0, len(self.cartas)-1))
        random.shuffle(self.cartas)

    def draw_card(self):
        if len(self.cartas) > 0:
            return self.cartas.pop(0)
        raise Exception("Não há mais cartas no monte")

    def compare_hands(self, *players):
        # TODO comparar mãos finais
        pass
