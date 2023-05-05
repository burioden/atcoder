n = int(input())
a = sorted(list(map(int,input().split())))

flg = 1

for i in range(n):
  if a[i] != i+1:
    flg = 0

print('Yes' if flg else 'No')
