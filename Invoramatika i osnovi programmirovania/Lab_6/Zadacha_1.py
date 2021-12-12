def Zadacha_1():
	import random
	lst = []
	while len(lst) <4:
		r= random.randint(1,9)
		if r not in lst: lst.append(r)
	print(lst)

	import Dop
	Dop.vixod()
