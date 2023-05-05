a,b,c,d,e,f,x = map(int, input().split())

takahashi = 0
aoki = 0

for i in range(1,x+1):
  if i%(a+c) <= a and i%(a+c) != 0:
    takahashi += b
  elif i%(a+c) > a and i%(a+c) == 0:
    takahashi += 0
  if i%(d+f) <= d and i%(d+f) != 0:
    aoki += e
  elif i%(d+f) > d and i%(d+f) == 0:
    aoki += 0
    
if takahashi > aoki:
  print('Takahashi')
elif takahashi < aoki:
  print('Aoki')
else:
  print('Draw')
