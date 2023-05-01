v,a,b,c = map(int, input().split())

v = v%(a+b+c)

if v<a:
    print("F")
elif v<a+b:
    print("M")
else:
    print("T")
