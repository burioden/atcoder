'''
なるほど理解した。
今しか見ておらず、今と次の締め切りを比較するの忘れていた…
'''

n = int(input())
d = []
m = 0
for i in range(n):
  a, b = map(int,input().split())
  d.append([b,-a])
  m = max(b,m)

d.sort(reverse=1)

for i, x in d:
  m = min(i, m)
  m += x
  if m < 0:
    print('No')
    exit()

print('Yes')
