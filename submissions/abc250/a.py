h,w = map(int,input().split())
r,c = map(int,input().split())

c = [[r-1,c],[r,c+1],[r+1,c],[r,c-1]]

cnt = 0
for i,d in c:
  if 0 < i <= h and 0 < d <= w:
    cnt += 1

print(cnt)
