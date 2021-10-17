def Lab_1_1():
  Isx_Str = 'xxpuxxasdxxx'
  New_Str = ''
  print(Isx_Str)
  for i in Isx_Str:
    if i == 'x':
      New_Str += 'y'
    else:
      New_Str += i
  print(New_Str)

Lab_1_1()