a,b,k = map(int, input().split())

def f(n,m):
    d = []
    for i in range(1, max(n,m)+1):
        if n % i == 0 and m % i == 0:
            d.append(i)
    return d

ans = f(a,b)

print(sorted(ans,reverse=True)[k-1])
