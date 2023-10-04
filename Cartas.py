class Spy:

    def __init__(self):
        self.valor = 0

    def validate(self, cards):
        return True



class Guard:

    def __init__(self):
        self.valor = 1

    def validate(self, cards):
        return True


class Priest:

    def __init__(self):
        self.valor = 2

    def validate(self, cards):
        return True

class Baron:

    def __init__(self):
        self.valor = 3

    def validate(self, cards):
        return True


class Handmaid:

    def __init__(self):
        self.valor = 4

    def validate(self, cards):
        return True

class Prince:

    def __init__(self):
        self.valor = 5

    def validate(self, cards):
        for card in cards:
            if type(card) == Countess:
                return False
        return True


class Chancellor:

    def __init__(self):
        self.valor = 6

    def validate(self, cards):
        return True

class King:

    def __init__(self):
        self.valor = 7

    def validate(self, cards):
        for card in cards:
            if type(card) == Countess:
                return False
        return True

class Countess:

    def __init__(self):
        self.valor = 8

    def validate(self, cards):
        return True


class Princess:

    def __init__(self):
        self.valor = 9

    def validate(self, cards):
        return False