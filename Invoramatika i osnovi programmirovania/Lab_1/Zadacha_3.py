def Zadacha_3():
# Description 
	print("Введите 3 числа: ");

# Input
	number_1 = int(input());
	number_2 = int(input());
	number_3 = int(input());

# Base
	if (number_1 < number_2) & (number_1 < number_3):
		print("Наименьшее: ");
		print(number_1);
	elif (number_2 < number_1) & (number_2 < number_3):
		print("Наименьшее: ");
		print(number_2);
	elif (number_3 < number_2) & (number_3 < number_1):
		print("Наименьшее: ");
		print(number_3);
		
	import Startovoia;
	Startovoia.Start();