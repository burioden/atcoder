x,y = map(int, input().split())

a = y-(2*x)
kame = a//2
turu = x-kame

if (kame*4)+(turu*2) == y and not kame < 0 and not turu < 0:
  print('Yes')
else:
  print('No')
