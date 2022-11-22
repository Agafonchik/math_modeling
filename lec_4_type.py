#типы данных: изменяемые(mutable) и неизменяемые(unmutable)
#complex - комплексные числа,  turple - кортежи, нельзя изменять
def changer(a, b):
    a = 2
    b[0] = 'good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])
print(L)

# комплексные числа
x = 3
y = 4
z = complex(x, y)
print(z)

w = complex(y, z)
print(w)
print(z + w)

# Strings - строки
s = 'hello'
print(s[0])

#s[0] = 'H' - неизменяемые типы данных
#print(s[0])

# Tuple 
t = (1, 4, 9)
print(t)
print(t[0])
#t[0] = 3

# Dict - словари
d = {'al':4, 4:'al', 'str':'hello'}
print(d[4])

d['str'] = 'good'
print(d)