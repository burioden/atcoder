n = int(input())
a = list(map(int,input().split()))

flg = 1

for i in range(n):
  if a[i]%2 == 0:
    if a[i]%3 == 0:
      continue
    elif a[i]%5 == 0:
      continue
    else:
      flg = 0
      break

print('APPROVED' if flg else 'DENIED')
