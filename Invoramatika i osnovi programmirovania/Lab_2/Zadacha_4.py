def Zadacha_4():
	# Description
	print("Введите целое число из диапазона [1, 9]: ");
	# Input
	number = int(input());

	# Base
	print("____________");
	if (1 <= number <= 9):
		for i in range(1, number + 1):
			print(str(i) * i);
	print("____________");
	import Startovoia;
	Startovoia.Start();