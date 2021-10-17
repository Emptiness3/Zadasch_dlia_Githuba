def Zadacha_3():
	# Description
	print("Введите целое число из диапазона [1, 1000]: ");
	# Input
	number = int(input());
	chislo_delitelei = 0;

	# Base
	if (1 <= number <= 1000):
		for i in range(1, number):
			if (number % i == 0):
				chislo_delitelei += i;
	else: print("Число не входит в диапазон [1, 1000], повторите запрос");

	if (chislo_delitelei == number):
		print(str(number) + " - " + "Это число совершенное");
	elif (chislo_delitelei != 0): 
		print("Число" + " " + str(number) + " " + "не является совершенным");


	import Startovoia;
	Startovoia.Start();