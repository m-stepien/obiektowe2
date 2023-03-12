from Pet import Pet

pet = Pet("Delta")

game_on = True


def get_valid_ans():
	result =input()
	try:
		result = int(result)
		if result in [1,2,3,0,955]:
			return result
		else:
			print("Wybierz poprawna opcje")

	except:
		print("Wybierz poprawna opcje")

def pet_eat(pet):
	loop = True
	print("Podaj wielkość posiłku jako liczba")
	while loop:
		try:
			num = int(input())
			loop = False
		except:
			print("Nie jest to liczba")
	pet.eat(num)

def pet_play(pet):
	loop = True
	print("Podaj czas zabawy jako liczba")
	while loop:
		try:
			num = int(input())
			loop = False
		except:
			print("Nie jest to liczba")
	pet.play(num)

while game_on:
	print("1. Sprawdz stan zwierzaka\n2.Nakarm go\n3.Baw sie\n0. wyjdz")
	choice = get_valid_ans()
	if choice == 1:
		pet.talk()
	elif choice == 2:
		pet_eat(pet)
	elif choice == 3:
		pet_play(pet)
	elif choice == 955:
		print(pet)
	elif choice == 0:
		game_on = False

