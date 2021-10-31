# Descriptions
import Text;
import Zadacha_1;
import Zadacha_2;
import Zadacha_3;
import Zadacha_4;
import Zadacha_5;
import Dop;
def Start():
	Text.Opisanie();

# Input
	Nomer = int(input());
	print("");

# Base 
	if (Nomer == 1):
		#print_zadacha_();
		print("Вы выбрали задачу 1");
		Zadacha_1.Zadacha_1();
	elif (Nomer == 2):
		#print_zadacha_();
		print("Вы выбрали задачу 2");
		Zadacha_2.Zadacha_2();
	elif (Nomer == 3):
		#print_zadacha_();
		print("Вы выбрали задачу 3");
		Zadacha_3.Zadacha_3();
	elif (Nomer == 4):
		#print_zadacha_();
		print("Вы выбрали задачу 4");
		Zadacha_4.Zadacha_4();
	elif (Nomer == 5):
		#print_zadacha_();
		print("Вы выбрали задачу 5");
		Zadacha_5.Zadacha_5();

Start();