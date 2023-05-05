def f(n):
    d = []
    for i in range(1,n+1):
        if i * i > n:
            break
        if n % i != 0:
            continue
        d.append(i)
        if n // i != i:
            d.append(n // i)
    d.sort()
    return d
  
print(*f(int(input())),sep="\n")
