n = int(input())

x = str(n//10//10)*3
x = int(x)

if n-x < 1:
  print(x)
else:
  print(x+111)
