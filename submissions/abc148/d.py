n = int(input())
a = list(map(int,input().split()))

cnt = n
m = 1

for i in a:
  if i == m:
    cnt -= 1
    m += 1
    
print(cnt if cnt != n else -1)
