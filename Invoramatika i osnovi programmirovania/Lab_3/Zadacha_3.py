def Zadacha_3():
    # Input
    height = int(input('Введите высоту пирамиды: '))
    # Base
    i = 0
    for r in range(height):
        print((height-r-1)*' ' + (i*2+1)*'X')
        i += 1

    import Startovoia;
    Startovoia.Start();