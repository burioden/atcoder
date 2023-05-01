r,c = map(int, input().split())
a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())

li = [[a1,a2],[b1,b2]]

print(li[r-1][c-1])
