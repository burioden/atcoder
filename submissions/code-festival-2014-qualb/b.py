n, k = map(int, input().split())
cnt = 0
for i in range(n):
  a = int(input())
  cnt += a
  if cnt >= k:
    exit(print(i + 1))
