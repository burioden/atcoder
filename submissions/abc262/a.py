n = int(input())

if (n+2) % 4 == 0:
  print(n)
elif (n+2) % 4 == 1:
    print(n+3)
elif (n+2) % 4 == 2:
    print(n+2)
else:
    print(n+1)
