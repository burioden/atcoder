a,b,c,d = map(int, input().split())

x = min(b,d) - max(a,c)

print(x if x > 0 else 0)
