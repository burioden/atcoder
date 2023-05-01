a,b,k = map(int, input().split())

i = a
ii = max(b-k+1,a+k)

while i <= min(b,a+k-1):
  print(i)
  i += 1
while ii <= b:
  print(ii)
  ii += 1
