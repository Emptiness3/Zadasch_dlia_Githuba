def Zadacha_2():
    # Input
    x = int(input('Введите количество столбцов в таблице: '))
    y = int(input('Введите количество строк в таблице: '))
	# Base
    for index1 in range(1, y+1):
        for index2 in range(1, x+1):
            print("%4d" % (index1 * index2), end='')
        print()
    
    import Dop;
    Dop.vixod();