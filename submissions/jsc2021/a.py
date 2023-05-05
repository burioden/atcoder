x,y,z = map(int, input().split())

print(int((y/x)*z-1) if ((y/x)*z) == int(((y/x)*z)) else int((y/x)*z))
