from CoinWithValue import CoinWithValue

class HazardGame:
    def __init__(self):
        self.money = 0
        self.coinList = [CoinWithValue(1), CoinWithValue(2), CoinWithValue(5)]

    def round(self):
        for coin in self.coinList:
            coin.throw()
            if coin.side == "orzel":
                self.money += coin.value
                coin.print_value_and_side()

    def game(self):
        while self.money < 20:
            self.round()
        if self.money==20:
            print("Gratuluje wygrales")
            result = True
        else:
            print("Gratulacje przegrales")
            result = False
        return result
