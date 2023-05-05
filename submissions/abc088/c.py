# 行と列の差

a = [list(map(int, input().split())) for _ in range(3)]

x = a[0][1] - a[0][0]
y = a[0][2] - a[0][1]

flg = 1

for i in range(1,3):
    if a[i][0] + x != a[i][1]:
      flg = 0
    if a[i][1] + y != a[i][2]:
      flg = 0
      
print('Yes' if flg else 'No')
