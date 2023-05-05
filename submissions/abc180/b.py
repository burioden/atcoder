n = int(input())
a = list(map(int,input().split()))

m = 0
y = 0
c = 0

for i in a:
  m += abs(i)
  y += abs(i)**2
  c = max(c,abs(i))


print(m)
print(y**0.5)
print(c)
