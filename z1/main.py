from Coin import Coin
from HazardGame import HazardGame

c1 = Coin()
c2 = Coin()
c3 = Coin()

for i in range(0, 14):
    c1.throw()
    print(c1)

# symulacja


win = 0
lose = 0
for x in range(1, 100):
    h_game = HazardGame()
    res = h_game.game()
    if res:
        print(str(x) + ' wygrana')
        win += 1
    else:
        lose += 1
        print(str(x) + ' przegrana')
print("Liczba wygranych {} \nLiczba przegranych {}".format(win, lose))