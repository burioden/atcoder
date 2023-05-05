n = int(input())
s = []
for i in range(n):
  a,b = input().split()
  b = int(b)
  s.append([a,-b,i+1])

s = sorted(s)

for i,d,k in s:
  print(k)
