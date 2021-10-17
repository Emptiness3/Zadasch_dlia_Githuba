def Zadacha_4():
	# Input
	chislo = int(input());

	# Base
	if (1 <= chislo <= 9):
		for i in range(1, chislo + 1):
			print(str(i) * i);

	import Startovoia;
	Startovoia.Start();