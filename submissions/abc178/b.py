a,b,c,d = map(int, input().split())

li = []
li.append(a*c)
li.append(a*d)
li.append(b*c)
li.append(b*d)

print(max(li))
