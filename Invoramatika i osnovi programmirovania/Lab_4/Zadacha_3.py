def Zadacha_3():
    for i in range(1,3000):  
        ct = 0
        n = 343**5+7**3-1-i
        while n>0:
            if n%7 == 6:
                ct+=1
            n = n//7
        if ct == 12:
            print(i)
            break

    import Dop
    Dop.vixod()
