def Zadacha_2():
# Description
	print("Введите ваши числа: ");

# Input
	chislo_1 = int(input());
	chislo_2 = int(input());
	result = "";

# Base
	if (chislo_1 > chislo_2) & (chislo_1 % chislo_2 == 0):
		result = str(chislo_1) + " кратно " + str(chislo_2);
		print(result);
	elif (chislo_2 > chislo_1) & (chislo_2 % chislo_1 == 0):
		result = str(chislo_2) + " кратно " + str(chislo_1);
		print(result);
		
	import Startovoia;
	Startovoia.Start();