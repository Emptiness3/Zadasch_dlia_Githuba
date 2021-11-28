import random;

Imia_v = input('Введите имя - ')
Rost_v = int(input('Введите рост - '))

class Students:
	def __init__(self, idy, imia, rost):

		self.idy = idy
		St_idy = self.idy
		self.imia = imia
		St_imena = self.imia
		self.rost = rost
		St_rosti = self.rost

		if ((St_imena == Imia_v) and (St_rosti - 5 < Rost_v < St_rosti + 5)):
			person = (St_idy, St_imena, rost)
			print(person)

Misha   = Students(0, "Misha", 178)
Natasha = Students(1, "Natasha", 160)
Natasha = Students(2, "Natasha", 160)
Vasilii = Students(3, "Vasilii", 180)
Vasilii = Students(4, "Vasilii", 183)
Valeria = Students(5, "Valeria", 158)
Valeria = Students(6, "Valeria", 170)


