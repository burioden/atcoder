h,w = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(h)]

flg = 1

for i in range(h-1):
  for j in range(w-1):
    if a[i][j]+a[i+1][j+1] > a[i+1][j]+a[i][j+1]:
      flg = 0
      break

print('Yes' if flg else 'No')
