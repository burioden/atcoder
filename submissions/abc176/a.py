n,x,t = map(int, input().split())

print(t*(n//x+1) if n%x != 0 else t*(n//x))
