import math

a,b = map(int,input().split())

d = math.sqrt((a**2)+(b**2))
A = '{:.6f}'.format(a/d)
B = '{:.6f}'.format(b/d)

print(A,B)
