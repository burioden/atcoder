n, a, b = map(int, input().split())

countH = n*a
countW = n*b

o_li = []
e_li = []

while countW >= b:
    countW -= b
    o_li.append("."*b)
    e_li.append("#"*b)
    if n >= 2 and countW >= b:
        countW -= b
        o_li.append("#"*b)
        e_li.append("."*b)

while countH >= a:
    for i in range(a):
        print("".join(map(str, o_li)))
    countH -= a
    if countH >= 1:
        for l in range(a):
            print("".join(map(str, e_li)))
        countH -= a
    else:
        break
