n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
  for j in range(i+1,n):
    if -1 <= (a[j][1] - a[i][1]) / (a[j][0] - a[i][0]) <= 1:
      cnt += 1
      
print(cnt)
