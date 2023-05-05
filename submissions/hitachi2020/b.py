a,b,m = map(int, input().split())
cool = list(map(int,input().split()))
hot = list(map(int,input().split()))
d = [list(map(int, input().split())) for _ in range(m)]

ans = min(cool) + min(hot)

for i in d:
  x = cool[i[0]-1] + hot[i[1]-1] - i[2]
  ans = min(ans,x)

print(ans)
