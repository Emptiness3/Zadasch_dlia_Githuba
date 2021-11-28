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

		count = 0
		len_0 = len(Imia_v)
		len_1 = len(St_imena)
		elem_0 = str(Imia_v)
		elem_1 = St_imena
		Vivod = 0

		if len_0 > len_1:
			max_len = len_0
		else:
			max_len = len_1

		for i in range(max_len):
			try:
				if elem_0[i] == elem_1[i]:
					count += 1
			except:
				pass

		Vivod = count / len_1; # деление кол-ва на длину для пропуска
	
		if ((St_rosti - 5 < Rost_v < St_rosti + 5) and (Vivod >= 0.4)):
			person = (St_idy, St_imena, rost)
			print(person)
			print(Vivod)

Misha   = Students(0, "Misha", 178)
Natasha = Students(1, "Natasha", 160)
Natasha = Students(2, "Natasha", 160)
Vasilii = Students(3, "Vasilii", 180)
Vasilii = Students(4, "Vasilii", 183)
Valeria = Students(5, "Valeria", 158)
Valeria = Students(6, "Valeria", 170)