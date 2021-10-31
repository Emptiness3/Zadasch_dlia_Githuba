def Zadacha_5():
    # Input
    while True:
        rub = int(input('Введите число в диапазоне [0;100]: '))
        if 0 <= rub <= 100:
            break
        else:
            print('Введено некорректное число')
    # Base
    if rub % 10 == 1 and rub != 11:
        print('{0} рубль'.format(rub))
    elif rub % 10 == 2 and rub !=12:
        print('{0} рубля'.format(rub))
    elif rub % 10 == 3 and rub !=13:
        print('{0} рубля'.format(rub))
    elif rub % 10 == 4 and rub !=14:
        print('{0} рубля'.format(rub))
    else:
        print('{0} рублей'.format(rub))

    import Startovoia;
    Startovoia.Start();