n = int(input())
a = [input() for _ in range(n)]

o = ['H' , 'D' , 'C' , 'S']
e = ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']

flg = 1
if len(set(a)) != n:
  flg = 0
for i in a:
  if i[0] not in o:
    flg = 0
  elif i[1] not in e:
    flg = 0

print('Yes' if flg else 'No')
