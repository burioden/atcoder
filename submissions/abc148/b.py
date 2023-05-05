n = int(input())
a,b = input().split()

s = []

for i in range(n):
  s.append(a[i])
  s.append(b[i])

print(*s,sep='')
