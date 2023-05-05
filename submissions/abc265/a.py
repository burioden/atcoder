x,y,n = map(int, input().split())

o = n//3

print(min(x*n,(y*o) + x*(n%3)))
