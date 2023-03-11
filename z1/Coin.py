import random


class Coin:
    def __init__(self):
        self.side = None

    def throw(self):
        self.side = random.choice(['orzel', 'reszka'])

    def __str__(self):
        return self.side
