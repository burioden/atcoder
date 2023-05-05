a,b = map(int,input().split())

a = list(map(int,str(a)))[::-1]
b = list(map(int,str(b)))[::-1]

A = 19-len(a)
B = 19-len(b)

a.extend([0]*A)
b.extend([0]*B)

flg = 1

for i in range(19):
  x = a[i] + b[i]
  if x >= 10:
    flg = 0
    break
  
print('Easy' if flg else 'Hard')
