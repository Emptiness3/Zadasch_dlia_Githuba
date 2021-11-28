def Zadacha_1():
	'Сумма чисел из блокнота'
	with open('Chisla.txt') as file:
		res = 0
		for line in file:
			res += sum(map(int, line.split()))
	print(res)

	import Dop
	Dop.vixod()
