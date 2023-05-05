'''
片方だけ決めれば一意に定まる
'''

s, p = map(int, input().split())

for n in range(int(p ** 0.5) + 1):
  m = s - n
  if m * n == p:
    exit(print('Yes'))

print('No')
