def Zadacha_3():
# Description 
	print("Введите ваши 3 числа: ");

# Input
	chislo_1 = int(input());
	chislo_2 = int(input());
	chislo_3 = int(input());

# Base
	if (chislo_1 < chislo_2) & (chislo_1 < chislo_3):
		print("Наименьшее: ");
		print(chislo_1);
	elif (chislo_2 < chislo_1) & (chislo_2 < chislo_3):
		print("Наименьшее: ");
		print(chislo_2);
	elif (chislo_3 < chislo_2) & (chislo_3 < chislo_1):
		print("Наименьшее: ");
		print(chislo_3);
		
	import Startovoia;
	Startovoia.Start();