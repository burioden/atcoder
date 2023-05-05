a = [list(map(int, input().split())) for _ in range(4)]

flg = 1

for i in range(4):
  x1,y1 = a[i-2]
  x2,y2 = a[i-1]
  x3,y3 = a[i]
  if (x3-x2)*(y1-y2) - (y3-y2)*(x1-x2) <= 0:
    flg = 0
    break
  
print('Yes' if flg else 'No')
