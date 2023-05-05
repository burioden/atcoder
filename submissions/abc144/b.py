n = int(input())

flg = 0

for i in range(1,10):
  for l in range(1,10):
    if i*l == n:
      flg = 1
      break

print('Yes' if flg else 'No')
