def Zadacha_4():
# Description
  print("Введите длины сторон: ");

# Input
  st_1 = int(input());
  st_2 = int(input());
  st_3 = int(input());
# Base  
  if ((st_1 + st_2) > st_3) & ((st_2 + st_3) > st_1) & ((st_3 + st_1) > st_2):
    print("Со сторонами: " + str(st_1) + ", " + str(st_2) + ", " + str(st_3) + ", можно построить треугольник");
  else: 
    print("Со сторонами: " + str(st_1) + ", " + str(st_2) + ", " + str(st_3) + ", невозможно построить треугольник");

  import Startovoia;
  Startovoia.Start();
