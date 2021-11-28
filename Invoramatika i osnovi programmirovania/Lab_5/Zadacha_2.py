def Zadacha_2():
    width = int(input('Введите ширину таблицы: '))
    height = int(input('Введите высоту таблицы: '))
    import random
    with open("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/Chisla2.txt", 'w') as file:
        for i in range(height):
            for j in range(width):
                file.write(str(random.randint(-100,100)) + ' ')
            file.write('\n')
    import Dop
    Dop.vixod()