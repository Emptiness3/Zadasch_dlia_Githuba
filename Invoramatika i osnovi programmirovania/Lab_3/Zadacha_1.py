def Zadacha_1():
	# Input
	s = 'Аргентина +++----манит ====:;*****"""негра.,!!!????'
	spez= '.,!?-+*= :;"'
	spez_2= "'"
	otvet= []

	# Base

	for i in range(len(s)):
		if s[i] not in spez:
			if s[i] not in spez_2:
				otvet.append(s[i])
	line = ''.join(otvet)
	line = line.lower()	
	elline = line[::-1]
	print(elline);
	print(line);

	if line == elline:
		print("Текст являеттся палиндромом")
	else:
		print("Текст не является палиндромом")

	import Dop;
	Dop.vixod();