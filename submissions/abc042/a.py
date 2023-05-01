a,b,c = list(map(int, input().split()))

if a==5:
    if b==5:
        if c==7:
            print("YES")
    elif b==7:
        if c==5:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
elif a==7:
    if b==5:
        if c==5:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
