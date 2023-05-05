n = int(input())

def f(n):
    d = 0
    for i in range(1, n+1):
        if n % i == 0:
            d += 1
    return d

cnt = 0
for i in range(105,n+1,2):
  x = f(i)
  if x == 8:
    cnt += 1

print(cnt)
