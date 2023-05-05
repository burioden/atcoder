a,b = map(int,input().split())

if a < 0 < b:
    print(abs(a)+abs(b)-1)
else:
    print(abs(abs(b)-abs(a)))
