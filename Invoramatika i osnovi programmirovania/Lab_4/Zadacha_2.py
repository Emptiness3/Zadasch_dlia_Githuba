def Zadacha_2(num):
	chislo = 0

	for i in range(len(num)):
		chislo += int(num[i]) * (2**(len(num) - i - 1))

	print('Число в десятичной системе = ' + str(chislo))

	import Dop
	Dop.vixod()