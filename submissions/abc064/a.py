a,b,c = map(int, input().split())
a = a*100
b = b*10
f = a+b+c

if f%4==0:
	print("YES")
else:
	print("NO")
