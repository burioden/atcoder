n = int(input())
li = [input() for i in range(n)]

flg = 1

if len(set(li)) < n:
  flg = 0
for i in range(1,n):
  if li[i][0] != li[i-1][-1]:
    flg = 0
    break

print('Yes' if flg else 'No')
