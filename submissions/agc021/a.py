n = int(input())
k = len(str(n))
c = str(n)[0]
s = int(c+"9"*(k-1))

if n == s:
  print(int(c)+9*(k-1))
else:
  print(int(c)+9*(k-1)-1)
