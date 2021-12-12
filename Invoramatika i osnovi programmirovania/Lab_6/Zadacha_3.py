def Zadacha_3():
    digits = {
        0: ('XXX', 'X X', 'X X', 'X X', 'XXX'),
        1: ('  X', ' XX', '  X', '  X', '  X'),
        2: ('XXX', '  X', ' X ', 'X  ', 'XXX'),
        3: ('XXX', '  X', 'XXX', '  X', 'XXX'),
        4: ('X X', 'X X', 'XXX', '  X', 'XXX'),
        5: ('XXX', 'X  ', 'XXX', '  X', 'XXX'),
        6: ('XXX', 'X  ', 'XXX', 'X X', 'XXX'),
        7: ('XXX', '  X', '  X', '  X', '  X'),
        8: ('XXX', 'X X', 'XXX', 'X X', 'XXX'),
        9: ('XXX', 'X X', 'XXX', '  X', 'XXX'),
    }
    def vivod_nomer(nomer):
        for i in range(len(digits[0])):
            for obj in nomer:
                print(digits[int(obj)][i].ljust(6, ' '), end='')
            print()


    def vvod_nomer():
        nomer = input('Введите номер: ')
        vivod_nomer(nomer)


    vvod_nomer()

    import Dop
    Dop.vixod()