def Zadacha_4():
    # Input
    lin = str(input('Введите предложение:\n'))

    # Base
    soglasnie = ['б', 'в', 'г', 'д', 'ж',
                 'з', 'й', 'к', 'л', 'м',
                 'н', 'п', 'р', 'с', 'т',
                 'ф', 'х', 'ц', 'ч' ,'ш', 'щ']
    glasnie =  ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    countGlas = 0
    countSogl = 0
    lin = lin.lower()
    for smb in lin:
        if smb in soglasnie:
            countSogl += 1
        if smb in glasnie:
            countGlas +=1
    if countGlas > countSogl:
        print('Строка гласная')
    elif countGlas < countSogl:
        print('Строка согласная')
    else:
        print('Гласных и согласных букв одинаковое кол–во')

    import Startovoia;
    Startovoia.Start();