e = set(input().split())
b = input()
l = set(input().split())

x = e & l
n = len(x)

if n == 6:
  print(1)
elif n == 5:
  if b in l:
    print(2)
  else:
    print(3)
elif n == 4:
  print(4)
elif n == 3:
  print(5)
else:
  print(0)
