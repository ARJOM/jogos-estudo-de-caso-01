class Player:

    def __init__(self, nome=""):
        self.nome = nome
        self.cartas = []
        self.mesa = []

    def __str__(self):
        return self.nome

    def use_card(self, card_index):
        carta = self.cartas[card_index]
        if not carta.validate(self.cartas):
            raise Exception("Essa carta não pode ser escolhida")
        self.mesa.append(self.cartas.pop(card_index))


    def add_card(self, card):
        self.cartas.append(card)
