f0 = 1
f1 = 1
n = 6

for m in range(n):
  f2 = f0 + f1
  f0 = f1
  f1 = f2
  print(f2)