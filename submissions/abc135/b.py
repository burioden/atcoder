n = int(input())
a = list(map(int,input().split()))

b = sorted(a)

cnt = 0
for i in range(n):
  if a[i] != b[i]:
    cnt += 1

print('YES' if cnt <= 2 else 'NO')
