def Zadacha_6():
	# Input
	chislo_1 = int(input());
	chislo_2 = int(input());
	a = 0;
	b = 0;
	del_1 = 0;
	del_2 = 0;
	prom_chislo = 0;

	# Base
	a = min(chislo_1, chislo_2);
	b = max(chislo_1, chislo_2);

	if (100000 <= a <= 200000) and (100000 <= b <= 200000):
		for i in range(a, b + 1):
			for i2 in range(2, i):
				if (i % i2 == 0):
					prom_chislo += 1;
					if (prom_chislo == 1):
						del_1 = i2;
					elif (prom_chislo == 2):
						del_2 = i2;
				if (prom_chislo > 2):
					prom_chislo = 0;
					break;	
			if (prom_chislo == 2):
				print("Число" + " " + str(i) + " " + "имеет два делителя, это" + ": " + str(del_1) + " и " + str(del_2));
			else: prom_chislo = 0;
	else: print("Числа вышли за диапазон! Введите числа в диапазоне [100 000, 200 000]");

	import Startovoia;
	Startovoia.Start();