#Написать функцию, которая вычисляет среднее арифметическое элементов одномерного массива, переданного ей в качестве аргумента.

a = [1, 2, 5, 875698766]

def byby(b):
    x = 0
    for i in b: 
        x = x + i
    return x
tmp = byby(a)
print(tmp)
