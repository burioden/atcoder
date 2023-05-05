n,k = map(int,input().split())

def f(N):
  x = str(N)
  s = int("".join(map(str,sorted(x))))
  l = int("".join(map(str,sorted(x,reverse=True))))
  return l-s

for i in range(k):
  n = f(n)
  
print(n)
