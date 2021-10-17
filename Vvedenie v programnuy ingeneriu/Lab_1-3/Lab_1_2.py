def Lab_1_2():
  chisla = [1, 3, 16, 25, 28, 30, 67, 300]
  x = 1
  for i in chisla:
    if i % 3 == 0 and i % 5 == 0:
      x *= i
  print(x)


Lab_1_2()