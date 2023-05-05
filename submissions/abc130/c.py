w,h,x,y = map(int,input().split())

z = h * w
a = z - (h * (w-x))
b = h * (w-x)
c = z - (w * (h-y))
d = w * (h-y)
e = (h * w)/2

ab = min(a,b)
cd = min(c,d)

menseki = max(ab,cd,e)

if a == b == c == d:
  nya = 1
else:
  nya = 0
  
print(menseki,nya)
