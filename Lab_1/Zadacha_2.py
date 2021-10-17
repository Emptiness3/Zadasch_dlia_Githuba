def Zadacha_2():
# Description
	print("Введите числа: ");

# Input
	number_1 = int(input());
	number_2 = int(input());
	result = "";

# Base
	if (number_1 > number_2) & (number_1 % number_2 == 0):
		result = str(number_1) + " кратно " + str(number_2);
		print(result);
	elif (number_2 > number_1) & (number_2 % number_1 == 0):
		result = str(number_2) + " кратно " + str(number_1);
		print(result);
	else: print("Числа не кратны")
		
	import Startovoia;
	Startovoia.Start();