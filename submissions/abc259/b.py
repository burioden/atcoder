from math import cos,pi,sin

a,b,d = map(int, input().split())

x = cos(pi*d/180)*a - sin(pi*d/180)*b
y = sin(pi*d/180)*a + cos(pi*d/180)*b

print(x,y)
