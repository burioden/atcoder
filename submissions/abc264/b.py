r,c = map(int,input().split())

x = abs(8-r)
y = abs(8-c)
z = max(x,y)

print('black' if z%2 == 1 else 'white')
