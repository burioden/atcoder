n = int(input())
a = sorted(list(map(int,input().split())))

ans = -1
mx = 0

for i in range(2,1001):
  s = sum(d%i == 0 for d in a)
  if mx < s:
    mx = s
    ans = i

print(ans)
