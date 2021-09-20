def Triangle(a, b, c):
    if b < a > c:
        return a < b + c
    elif a < b > c:
        return b < a + c
    else:
        return c < a + c
 
 
a = int(input())
b = int(input())
c = int(input())
print('Это треугольник' if Triangle(a, b, c) else "Это не треугольник")
