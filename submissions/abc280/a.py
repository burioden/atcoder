h,w = map(int,input().split())
a = [input() for _ in range(h)]

ans = 0
for i in a:
  ans += i.count("#")

print(ans)
