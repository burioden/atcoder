n = int(input())
p = list(map(int,input().split()))

cnt = 0
start = 0
x = 1
end = 2

while end < n:
  pp = sorted([p[start],p[x],p[end]])
  if pp[1] == p[x]:
    cnt += 1
  start += 1
  x += 1
  end += 1

print(cnt)
