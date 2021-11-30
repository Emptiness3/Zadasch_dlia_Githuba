Name_HE    = input("Введите имя: ");
SecName_HE = input("Введите фамилию: ");
Street_HE  = input("Введите название улицы: ");
House_HE   = int(input("Введите номер дома: "));
Floor_HE   = int(input("Введите номер квартиры: "));
print();


class Students:


	def __init__(self, idn, name, secName, street, house, floor):

		self.idn = idn;
		St_idn = self.idn;

		self.name = name;
		St_name = self.name;

		self.secName = secName;
		St_secName = self.secName;

		self.street = street;
		St_street = self.street;

		self.house = house;
		St_house = self.house;

		self.floor = floor;
		St_floor = self.floor;

### Algoritm Compare
		count = 0;

		len_0 = len(Name_HE);
		len_1 = len(name);
		len_2 = len(SecName_HE);
		len_3 = len(secName);
		len_4 = len(Street_HE);
		len_5 = len(street);

		len_sum = len_1 + len_3 + len_5;

		max_len = 0;

		elem_0 = str(Name_HE);
		elem_1 = St_name;
		elem_2 = SecName_HE;
		elem_3 = secName;
		elem_4 = Street_HE;
		elem_5 = St_street;

		Compare_return = 0;

		max_len = max(len_0, len_1, len_2, len_3, len_4, len_5);
	
		#print('Max: ' + str(max_len));

		for i in range(max_len):
			try:
				if elem_0[i] == elem_1[i]:
					count += 1;
			except:
				pass;
		print("Wawe 1: " + " Счётчик for_1: " + str(i) + "; Максимум длины: " + str(max_len) + "; Счётчик совпалдений: " + str(count)); # Debug

		for i2 in range(max_len):
			try:
				if elem_2[i2] == elem_3[i2]:
					count += 1;
			except:
				pass;
		print("Wawe 2: " + " Счётчик for_2: " + str(i2) + "; Максимум длины: " + str(max_len) + "; Счётчик совпалдений: " + str(count)); # Debug

		for i3 in range(max_len):
			try:
				if elem_4[i3] == elem_5[i3]:
					count += 1;
			except:
				pass;
		print("Wawe 3: " + " Счётчик for_3: " + str(i3) + "; Максимум длины: " + str(max_len) + "; Счётчик совпалдений: " + str(count)); # Debug

				#print(count)
		#print(max_len)
		Compare_return = count / len_sum;
		print('Compare_return: ' + str(Compare_return) + '\n'); # Debug


		if (Compare_return >= 0.3) and (St_house - 5 <= House_HE <= St_house + 5) or 	   (Compare_return >= 0.3) and (St_floor - 5 <= Floor_HE <= St_floor + 5):
			person = (St_idn, St_name, St_secName, St_street, St_house, St_floor);
			print(person);

###               ID --- Name --- SecName --- Street - House - Floor
Misha   = Students(0, "Misha", "Kuzmin", "Krupskoi", 69, 45)
Natasha = Students(1, "Natasha", "Mishina", "Habarovckaia", 56, 110)
Natasha = Students(2, "Natasha", "Pushkina", "Mira", 48, 52)
Vasilii = Students(3, "Vasilii", "Smrinov", "Maia", 23, 33)
Vasilii = Students(4, "Vasilii", "Krilov", "Kirova", 43, 21)
Valeria = Students(5, "Valeria", "Pavlova", "Odoevskogo", 44, 55)
Valeria = Students(6, "Valeria", "Kruskova", "Dokuchaeva", 55, 43)

