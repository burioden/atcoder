n,t = map(int,input().split())
a = [int(input()) for _ in range(n)]

b = []
for i in range(1,n):
  b.append(min(t,a[i] - a[i-1]))

print(sum(b)+t)
