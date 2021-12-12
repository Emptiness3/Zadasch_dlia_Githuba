# Descriptions
import Text
import Zadacha_1
import Zadacha_2
import Zadacha_3
import Dop
def Start():
	Text.Opisanie()

# Input
	Nomer = int(input())
	print("")

# Base 
	if (Nomer == 1):
		print("Вы выбрали задачу 1")
		Zadacha_1.Zadacha_1()
	elif (Nomer == 2):
		print("Вы выбрали задачу 2")
		Zadacha_2.Zadacha_2()
	elif (Nomer == 3):
		print("Вы выбрали задачу 3")
		Zadacha_3.Zadacha_3()
Start()