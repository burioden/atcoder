n,blue,red = map(int,input().split())

x = blue+red

print((n//x) * blue + min(blue,n%x))
