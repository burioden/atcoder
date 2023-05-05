n,a,b = map(int,input().split())
s = input()

f = [0]*n
z = a+b

for i in range(n):
  if s[i] == "a" and 0 < z:
    f[i] = 1
    z -= 1
  elif s[i] == "b" and 0 < z and 0 < b:
    f[i] = 1
    z -= 1
    b -= 1

for i in f:
  if i == 1:
    print('Yes')
  else:
    print('No')
