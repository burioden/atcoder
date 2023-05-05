n = int(input())
p = list(map(int,input().split()))

for i in reversed(range(n-1)):
  if p[i] > p[i+1]:
    j = i
    break

for i in reversed(range(n)):
  if p[j] > p[i]:
    k = i
    break

p[j],p[k] = p[k],p[j]

print(*p[:j+1],*p[:j:-1])
