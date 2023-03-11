from Coin import Coin


class CoinWithValue(Coin):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def print_value_and_side(self):
        print("{} : {}".format(self.value, self.side))
