x0 = 10 # переменная в глобальной области видимости (scope)

def move(t):
    x = x0 * t
    return x #локальная область видимости - тело функции

print(move(3))
#print(x) так как неглобально, что и не видит

a = 'good'

def my_fun():
    a = 'bad'
    print(a)

my_fun()
print(a)