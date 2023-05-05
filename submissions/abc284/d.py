t = int(input())

def f(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(t):
  n = int(input())
  
  for j in range(2,n):
    if n%j == 0: # 片方は当たり前にnの約数である
      if n%(j**2) == 0: # jはどちら側か
        p = j
        q = n//(j**2)
        if f(p) == 1: #素数か
          print(p, q)
          break
        break
      else:
        p = int((n//j)**0.5)
        q = j
        if f(p) == 1: #素数か
          print(p, q)
          break
        break
