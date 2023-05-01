n,x = map(int,input().split())

li = []

for i in range(65, 91):
    li += (chr(i)*n)

print(li[x-1])
