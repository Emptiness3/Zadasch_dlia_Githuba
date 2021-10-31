def Zadacha_4():
    # Input
    linia = str(input('Введите предложение:\n'))

    # Base
    soglasnie = ['б', 'в', 'г', 'д', 'ж',
                 'з', 'й', 'к', 'л', 'м',
                 'н', 'п', 'р', 'с', 'т',
                 'ф', 'х', 'ц', 'ч' ,'ш', 
                 'щ', ]
    glasnie =  ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    countGlas = 0
    countSogl = 0
    linia = linia.lower()
    for smb in linia:
        if smb in soglasnie:
            countSogl += 1
        if smb in glasnie:
            countGlas +=1
    if countGlas > countSogl:
        print('Линия содержит больше гласных')
    elif countGlas < countSogl:
        print('Линия содержит больше согласных')
    else:
        print('Количество гласных и согласных равно')

	import Dop;
	Dop.vixod();