def Zadacha_3():
    num = int(input('Введите номер столбца: '))
    from operator import itemgetter
    with open ("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/Chisla3.txt") as file:
        chisla = file.readlines()
        resultat = []
        for line in chisla:
            paral = line.strip().split()
            resultat.append(paral)
        for i in range(4):
            for j in range(6):
                [i][j] = int(resultat[i][j])
        with open("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/ChislaOtsor3.txt", 'w') as result:
            for obecti in sorted(resultat, key=itemgetter(num - 1), reverse=False):
                for i in range(len(obecti)):
                    if i != len(obecti) - 1:
                        result.write(str(obecti[i]) + ' ')
                    else:
                        result.write(str(obecti[i]) + '\n')

    import Dop
    Dop.vixod()