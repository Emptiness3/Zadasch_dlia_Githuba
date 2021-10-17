def Zadacha_2():
	# Description
	print("Введите число изи диапазона [1, 1000]: ");
	# Input
	chislo = int(input());
	prom_chislo = 0;

	# Base
	if (1 <= chislo <= 1000):
		for i in range(1, chislo + 1):
			if (chislo % i == 0):
				prom_chislo += 1;

	else: print("Число вышло за диапазон! Введите число в диапазоне [1, 1000]");

	if (prom_chislo == 2):
		print(str(chislo) + " - " + "Это число простое");
	elif (prom_chislo != 0): 
		print("У числа" + " " + str(chislo) + " " + "более двух делителей!");


	import Startovoia;
	Startovoia.Start();