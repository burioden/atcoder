n = int(input())
a = list(map(int,input().split()))

m = 2**n//2

A = max(a[:m])
B = max(a[m:])
C = min(A,B)

print(a.index(C)+1)
