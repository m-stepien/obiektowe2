from Die import Die
from Player import Player
from Cpu_player import Cpu_player


p1 = Player()
p2 = Cpu_player()
player_die = Die(6)
cpu_die = Die(6)
game_on = True
while p1.get_score()<=21 and p2.get_score()<=21 and game_on:
	print(p1.get_score())
	if not p1.get_block():
		p1.decide_want_stil_play()
		if p1.get_still_playing():
			player_die.roll()
			print(player_die)
			p1.add_to_score(player_die.get_value())
			if p1.get_score()>21:
				p1.block_playing()
		else:
			p1.block_playing()

	if not p2.get_block():
		p2.decide_want_stil_play()
		if p2.get_still_playing():
			cpu_die.roll()
			p2.add_to_score(cpu_die.get_value())
			if p2.get_score()>21:
				p2.block_playing()
		else:
			p2.block_playing()	
	if p2.get_block() and p1.get_block():
		game_on = False		


print("________________________________________________________")
print(p1.get_score())
print(p2.get_score())
if (p1.get_score()>21 and p2.get_score()>21) or (p1.get_score() == p2.get_score()):
	print("remis")

elif (p1.get_score()>p2.get_score() and p1.get_score()<=21) or p2.get_score()>21:
	print("wygral p1")

elif (p2.get_score()>p1.get_score() and p2.get_score()<=21) or p1.get_score()>21:
	print("wygral p2")





