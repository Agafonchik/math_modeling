a = int(input())
b = int(input())

if b == 0:
  print('на ноль делить нельзя')
elif a % b == 0:
  print('делится', a // b)
elif a % b != 0:
  print(f'не делится, {a % b}')