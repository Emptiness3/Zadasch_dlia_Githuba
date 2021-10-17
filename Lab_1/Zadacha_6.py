def Zadacha_6():
# Biblio
	import math;

# Description 
	print("Введите коэффиценты уравнения: ");

# Input
	a = int(input());
	b = int(input());
	c = int(input());
	koren_1 = 0;
	koren_2 = 0;
	D = 0;

# Base
	D = (b**2) - (4*a*c);
	if (D > 0):
		koren_1 = (((b-b*2) + math.sqrt(D)) / (2 * a));
		koren_2 = (((b-b*2) - math.sqrt(D)) / (2 * a));
		print("Первый корень: " + str(koren_1));
		print("Второй корень: " + str(koren_2));
	elif (D == 0):
		koren_1 = (((b-b*2)) / (2 * a));
		print("Один корень: " + str(koren_1));
	elif (D < 0):
		print("Нет корней");
		
	import Startovoia;
	Startovoia.Start();