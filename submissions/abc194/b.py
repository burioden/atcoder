n = int(input())
a = []
b = []
for i in range(n):
  A,B = map(int,input().split())
  a.append(A)
  b.append(B)

ans = 10**6

for i in range(n):
  for j in range(n):
    ans = min(ans,a[i]+b[j] if i==j else max(a[i],b[j]))

print(ans)
