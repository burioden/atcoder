n = int(input())
s = list(input())
q = int(input())

flg = False
for i in range(q):
  t,a,b = map(int, input().split())
  if t == 1:
    a -= 1
    b -= 1
    if flg == True:
      x = (n+a) % (n*2)
      y = (n+b) % (n*2)
      s[x],s[y] = s[y],s[x]
    else:
      s[a],s[b] = s[b],s[a]
  elif t == 2:
    flg ^= True

if flg:
  s[:n],s[n:] = s[n:],s[:n]
  
print(*s,sep='')
