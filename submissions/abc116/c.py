'''
・一番高いものの回数は絶対に必要
・というか区間なので、ひとつ前のものと比較して、高ければその差分を足していけばよい
'''

n = int(input())
h = list(map(int, input().split()))

cnt = 0
before = 0

for i in range(n):
  if h[i] > before:
    cnt += h[i] - before
  before = h[i]
  
print(cnt)
