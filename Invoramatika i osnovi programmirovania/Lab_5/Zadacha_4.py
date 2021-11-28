def Zadacha_4():
    with open("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/Vvod.txt", encoding='utf-8') as file:
        with open("c:/Users/misha/Desktop/Zadasch_dlia_Githuba/Zadasch_dlia_Githuba/Invoramatika i osnovi programmirovania/Lab_5/Vivod.txt", 'w', encoding='utf-8') as res:
            for li in file:
                text = li 
                spez= ['!', '?', '-', '+', '*', '=', ' ', ':',';', '.', ',', '"', "'", '\n']
                otvet= ''
                Izmen= []
                for sim in text:
                    if  sim not in spez:
                        Izmen.append(sim)
                otvet = ''.join(Izmen)
                otvet = otvet.lower()	
                if otvet == otvet[::-1]:
                    res.write(li)
    import Dop
    Dop.vixod()
