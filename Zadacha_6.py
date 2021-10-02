def Zadacha_6():
# Biblio
	import math;

# Description 
	print("Введите коэффиценты уравнения: ");

# Input
	a = int(input());
	b = int(input());
	c = int(input());
	x_1 = 0;
	x_2 = 0;
	D = 0;

# Base
	# a * x^2 + bx + c = 0
	D = (b**2) - (4*a*c);
	if (D > 0):
		x_1 = (((b-b*2) + math.sqrt(D)) / (2 * a));
		x_2 = (((b-b*2) - math.sqrt(D)) / (2 * a));
		print("Первый корень: " + str(x_1));
		print("Второй корень: " + str(x_2));
	elif (D == 0):
		x_1 = (((b-b*2)) / (2 * a));
		print("Единственный корень: " + str(x_1));
	elif (D < 0):
		print("Нет корней");
		
	import Startovoia;
	Startovoia.Start();