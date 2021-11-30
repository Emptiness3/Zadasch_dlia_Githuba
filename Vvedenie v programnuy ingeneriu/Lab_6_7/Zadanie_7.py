### Vvod dannih
Imia_v    = input("Введите имя - ")
Vamilia_v = input("Введите фамилию - ")
Uliza_v  = input("Введите название улицы - ")
Dom_v   = int(input("Введите номер дома - "))
Kvartira_v   = int(input("Введите номер квартиры - "))
print()


class Students:


	def __init__(self, idy, Imia, Vamilia, Uliza, Dom, Kvartira):

		self.idy = idy
		St_idy = self.idy

		self.Imia = Imia
		St_Imia = self.Imia

		self.Vamilia = Vamilia
		St_Vamilia = self.Vamilia

		self.Uliza = Uliza
		St_Uliza = self.Uliza

		self.Dom = Dom
		St_Dom = self.Dom

		self.Kvartira = Kvartira
		St_Kvartira = self.Kvartira

### Algoritm Sravnenia
		count = 0

		len_0 = len(Imia_v)
		len_1 = len(Imia)
		len_2 = len(Vamilia_v)
		len_3 = len(Vamilia)
		len_4 = len(Uliza_v)
		len_5 = len(Uliza)

		len_sum = len_1 + len_3 + len_5

		max_len = 0

		elem_0 = str(Imia_v)
		elem_1 = St_Imia
		elem_2 = Vamilia_v
		elem_3 = Vamilia
		elem_4 = Uliza_v
		elem_5 = St_Uliza

		Vivod = 0

		max_len = max(len_0, len_1, len_2, len_3, len_4, len_5)
	

		for i in range(max_len):
			try:
				if elem_0[i] == elem_1[i]:
					count += 1
			except:
				pass
		print("1: " + " Сумма for_1: " + str(i) + " Макс: " + str(max_len) + " Сумма сходств: " + str(count)); # Otladka

		for i2 in range(max_len):
			try:
				if elem_2[i2] == elem_3[i2]:
					count += 1
			except:
				pass
		print("2: " + " Сумма for_2: " + str(i) + " Макс: " + str(max_len) + " Сумма сходств: " + str(count)); # Otladka


		for i3 in range(max_len):
			try:
				if elem_4[i3] == elem_5[i3]:
					count += 1
			except:
				pass
		print("3: " + " Сумма for_3: " + str(i) + " Макс: " + str(max_len) + " Сумма сходств: " + str(count)); # Otladka


		Vivod = count / len_sum
		print('Vivod: ' + str(Vivod) + '\n'); # Otladka

### Algoritm Sravnenia Chislovih
		if (Vivod >= 0.3) and (St_Dom - 5 <= Dom_v <= St_Dom + 5) or (Vivod >= 0.3) and (St_Kvartira - 5 <= Kvartira_v <= St_Kvartira + 5):
			person = (St_idy, St_Imia, St_Vamilia, St_Uliza, St_Dom, St_Kvartira)
			print(person)
			print('     ')

### Baza dannih studentov
Misha   = Students(0, "Misha", "Kuzmin", "Krupskoi", 69, 45)
Natasha = Students(1, "Natasha", "Mishina", "Habarovckaia", 56, 110)
Natasha = Students(2, "Natasha", "Pushkina", "Mira", 48, 52)
Vasilii = Students(3, "Vasilii", "Smrinov", "Maia", 23, 33)
Vasilii = Students(4, "Vasilii", "Krilov", "Kirova", 43, 21)
Valeria = Students(5, "Valeria", "Pavlova", "Odoevskogo", 44, 55)
Valeria = Students(6, "Valeria", "Kruskova", "Dokuchaeva", 55, 43)

