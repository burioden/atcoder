from math import factorial

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))


def f(L):
    index = 0
    while len(L)> 1:
        a = len([l for l in L if l<L[0]])
        index = index + a * factorial(len(L) - 1)
        L = L[1:]
    return index

print(abs(f(p)-f(q)))
