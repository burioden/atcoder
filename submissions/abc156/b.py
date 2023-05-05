n,k = map(int,input().split())

cnt = 0
while 0 < n:
  n = n//k
  cnt += 1

print(cnt)
