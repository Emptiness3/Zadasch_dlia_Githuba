def Zadacha_5():
# Biblio
	import math;

# Description
	print("Введите радиус круга: ");

# Input
	radius = int(input());
	ploshad = 0; 
	dlina = 0;

# Base
	dlina = math.pi * 2 * radius;
	ploshad = math.pi * radius ** 2;
	print("Длина круга: " + str(dlina));
	print("Площадь круга: " + str(ploshad));
	
	import Startovoia;
	Startovoia.Start();