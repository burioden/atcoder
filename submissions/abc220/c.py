n = int(input())
a = list(map(int,input().split()))
x = int(input())

s = sum(a)
k = x//s
c = x%s

e = 0
for i,d in enumerate(a):
  e += d
  if c < e:
    print(k*n+i+1)
    break
