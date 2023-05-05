n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0

for i in range(n):
  x = a[i] * b[i]
  ans += x

print('Yes' if ans == 0 else 'No')
