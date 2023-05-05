n, x = map(int, input().split())
a = set(map(int, input().split()))
b = set()

for i in a:
  b.add(x + i)

flg = 0
for i in b:
  if i in a:
    flg = 1

print('Yes' if flg else 'No')
