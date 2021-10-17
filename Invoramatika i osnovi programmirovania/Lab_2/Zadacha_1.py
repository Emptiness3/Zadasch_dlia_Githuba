def Zadacha_1():
	# Description
	print("Введите два целых числа из диапозона [-100, 100]: ");
	# Input
	number_1 = int(input());
	number_2 = int(input());
	min_number = 0;
	max_number = 0;

	# Base
	min_number = min(number_1, number_2);
	max_number = max(number_1, number_2);

	if (-100 <= min_number <= 100) and (-100 <= max_number <= 100):
		for i in range(min_number, max_number + 1):
			if (i % 2 != 0):
				print(i);
	else: print("Числа не входят в диапазон [-100, 100], повторите запрос");

	import Startovoia;
	Startovoia.Start();