n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
  ans += li[i][1]-li[i][0]+1

print(ans)
