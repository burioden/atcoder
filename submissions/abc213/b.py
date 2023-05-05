n = int(input())
a = list(map(int,input().split()))

al = sorted(a)[-2]
ans = a.index(al)

print(ans+1)
