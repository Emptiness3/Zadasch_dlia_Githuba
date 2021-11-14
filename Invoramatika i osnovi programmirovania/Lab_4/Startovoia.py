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
		#print_zadacha_();
		print("Вы выбрали задачу 1")
		Zadacha_1.get_max(int(input('Введите положительное число: ')))
	elif (Nomer == 2):
		#print_zadacha_();
		print("Вы выбрали задачу 2")
		Zadacha_2.Zadacha_2(input('Введите двоичное число: '))
	elif (Nomer == 3):
		#print_zadacha_();
		print("Вы выбрали задачу 3")
		Zadacha_3.Zadacha_3()
Start();