def Lab_1_3():
  Stroka = 'xxpuxxasdxxx'
  print(Stroka)
  for i in Stroka:
    if i == 'x':
      Stroka = Stroka.replace(i, 'y')
  print(Stroka)


Lab_1_3()