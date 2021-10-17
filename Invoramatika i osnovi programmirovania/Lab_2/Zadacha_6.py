def Zadacha_6():
	# Description
	print("Введите два целых числа из диапозона [100000, 200000]: ");
	# Input
	number_1 = int(input());
	number_2 = int(input());
	a = 0;
	b = 0;
	delitel_1 = 0;
	delitel_2 = 0;
	chislo_delitelei = 0;

	# Base
	a = min(number_1, number_2);
	b = max(number_1, number_2);

	if (100000 <= a <= 200000) and (100000 <= b <= 200000):
		for i in range(a, b + 1):
			for i2 in range(2, i):
				if (i % i2 == 0):
					chislo_delitelei += 1;
					if (chislo_delitelei == 1):
						delitel_1 = i2;
					elif (chislo_delitelei == 2):
						delitel_2 = i2;
				if (chislo_delitelei > 2):
					chislo_delitelei = 0;
					break;	
			if (chislo_delitelei == 2):
				print("У числа" + " " + str(i) + " " + "два делителя, это" + ": " + str(delitel_1) + " и " + str(delitel_2));
			else: chislo_delitelei = 0;
	else: print("Числа не входят в диапазон [100 000, 200 000], повторите запрос");

	import Startovoia;
	Startovoia.Start();