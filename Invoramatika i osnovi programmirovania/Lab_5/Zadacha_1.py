def Zadacha_1():
	with open("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/Chisla.txt") as file:
		res = 0
		for line in file:
			res += sum(map(int, line.split()))
	print(res)

	import Dop
	Dop.vixod()
