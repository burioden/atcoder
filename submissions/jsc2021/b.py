n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = set(a) ^ set(b)

ans = sorted(list(ans))

print(' '.join(map(str, ans)))
