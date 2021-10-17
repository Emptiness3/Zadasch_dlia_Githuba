def Zadacha_5():
	# Input
	chislo = int(input());

	# Base
	if (1 <= chislo <= 9):
		for i in range(1, chislo + 1):
			print(str(chislo) * chislo);

	import Startovoia;
	Startovoia.Start();