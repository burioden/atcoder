'''
各カンマを打つところを観測
そこに至るまでの回数は全て足している、と考える
'''

n = int(input())
m = n

go = 0
yon = 0
san = 0
ni = 0
ichi = 0

a = 10**15
b = 10**12
c = 10**9
d = 10**6
e = 10**3

if n >= a:
  go = 1
elif n >= b:
  yon = n - b + 1
elif n >= c:
  san = n - c + 1
elif n >= d:
  ni = n - d + 1
elif n >= e:
  ichi = n - e + 1

ans = 0

if yon > 0:
  ans = (b + yon)*4 - b - c - d - e
elif san > 0:
  ans = (c + san)*3 - c - d - e
elif ni > 0:
  ans = (d + ni)*2 - d - e
elif ichi > 0:
  ans = ichi
elif go > 0:
  ans = (a + go)*5 - a - b - c - d - e
  
print(ans)
