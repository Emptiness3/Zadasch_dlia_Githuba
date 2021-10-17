def Zadacha_2():
	# Description
	print("Введите число из диапазона [1, 1000]: ");
	# Input
	number = int(input());
	chislo_deletilei = 0;

	# Base
	if (1 <= number <= 1000):
		for i in range(1, number + 1):
			if (number % i == 0):
				chislo_deletilei += 1;

	else: print("Число не входит в диапазон [1, 1000], повторите запрос");

	if (chislo_deletilei == 2):
		print(str(number) + " - " + "Это число простое");
	elif (chislo_deletilei != 0): 
		print("Число" + " " + str(number) + " " + "не является простым.");


	import Startovoia;
	Startovoia.Start();