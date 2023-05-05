import math

a,b,c,d = map(int, input().split())

x = a-1
y = c*d//(math.gcd(c,d))

print(b - (b//c + b//d) + b//y - (x-((x//c) + (x//d)) + x//y))
