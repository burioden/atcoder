n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, n):
  if a[i] - a[i - 1] <= m:
    exit(print(a[i]))

print(-1)
