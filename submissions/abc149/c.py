def f(n):
    p = True
    if n == 1:
        p = False
    else:
        for i in range(2, n):
            if n % i == 0:
                p = False
                break
    return p

n = int(input())

for i in range(n,998244353):
  if f(i) == True:
    print(i)
    break
