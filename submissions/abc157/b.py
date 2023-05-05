a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for i in range(n):
  x = int(input())
  for j in a:
    for k in range(3):
      if j[k] == x:
        j[k] = '.'

flg = 0

if a[0][0] == a[1][0] == a[2][0] == '.':
  flg = 1
elif a[0][1] == a[1][1] == a[2][1] == '.':
  flg = 1
elif a[0][2] == a[1][2] == a[2][2] == '.':
  flg = 1
elif a[0][0] == a[0][1] == a[0][2] == '.':
  flg = 1
elif a[1][0] == a[1][1] == a[1][2] == '.':
  flg = 1
elif a[2][0] == a[2][1] == a[2][2] == '.':
  flg = 1
elif a[0][0] == a[1][1] == a[2][2] == '.':
  flg = 1
elif a[0][2] == a[1][1] == a[2][0] == '.':
  flg = 1
  
print('Yes' if flg else 'No')
