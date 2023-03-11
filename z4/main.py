import pickle
from Smarthphone import Smarthphone

def put(list_of_phone):
	with open("phones.dat", "ab") as phones:
		for obj in list_of_phone:
			pickle.dump(sm1, phones)


def load():
	with open("phones.dat", "rb") as phones:
		list_of_phone = []
		while True:
			try:
				phone=pickle.load(phones)
				list_of_phone.append(phone)
			except:
				break
	return list_of_phone



sm1 = Smarthphone("Samsung", "S5", 400)
sm2 = Smarthphone("Apple", "I9", 100)
sm3 = Smarthphone("Goophone", "Z900", 454)
put([sm1, sm2, sm3])
new_list_of_phone = load()
print(len(new_list_of_phone))
for phone in new_list_of_phone:
	print(phone)
