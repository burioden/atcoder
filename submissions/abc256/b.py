n = int(input())
a = list(map(int,input().split()))

a = a[::-1]

cnt = 0
for i in range(1,n):
  a[i] += a[i-1]

for i in a:
  if i > 3:
    cnt += 1
print(cnt)
