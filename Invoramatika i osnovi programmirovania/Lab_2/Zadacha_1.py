def Zadacha_1():
	# Input
	chislo_1 = int(input());
	chislo_2 = int(input());
	min_chislo = 0; # Можно и без этого
	max_chislo = 0; # Можно и без этого

	# Base
	min_chislo = min(chislo_1, chislo_2);
	max_chislo = max(chislo_1, chislo_2);

	if (-100 <= min_chislo <= 100) and (-100 <= max_chislo <= 100):
		for i in range(min_chislo, max_chislo + 1):
			if (i % 2 != 0):
				print(i);
	else: print("Числа вышли за диапазон! Введите числа в диапазоне [-100, 100]");

	import Startovoia;
	Startovoia.Start();