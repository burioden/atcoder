n = int(input())
a = list(map(int,input().split()))

cnt = 0
m = n+1

for i in a:
  if m > i:
    m = i
    cnt += 1

print(cnt)
