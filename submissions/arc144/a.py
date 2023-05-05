n = int(input())

m = 2*n
if n%4 == 0:
  x = str('4'*(n//4))
else:
  x = str(n%4)+str('4'*(n//4))
  
print(m)
print(x)
