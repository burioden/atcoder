h,m = map(int,input().split())

h %= 12
h *= 30
h += m*0.5
m *= 6

print(min(abs(h-m),360 - abs(m-h)))
