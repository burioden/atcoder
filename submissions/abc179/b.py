n = int(input())

li = []

for i in range(n):
  x,y = map(int, input().split())
  d = abs(x-y)
  li.append(d)

flg = 0

for i in range(2,n):
  if li[i] == 0 and li[i-1] == 0 and li[i-2] == 0:
    flg = 1
    break

print('Yes' if flg else 'No')
