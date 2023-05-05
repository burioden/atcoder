a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

b *= 0.1
d *= 0.1
f *= 0.1

x = a*b
y = c*d
z = e*f

print(int(x+y+z))
