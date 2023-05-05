n = int(input())

cnt = 0
for _ in range(n):
  a = sum(list(map(int, input().split())))
  if a < 20:
    cnt += 1
    
print(cnt)
