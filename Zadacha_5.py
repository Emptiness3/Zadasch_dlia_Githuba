def Zadacha_5():
# Biblio
	import math;

# Description / Interface
	print("Введите радиус круга: ");

# Input
	radius = int(input());
	s = 0; # Площадь круга
	l = 0; # Длина окружности

# Base
	l = math.pi * 2 * radius;
	s = math.pi * radius ** 2;
	print("Длина окружности: " + str(l));
	print("Площадь круга: " + str(s));
	
	import Startovoia;
	Startovoia.Start();