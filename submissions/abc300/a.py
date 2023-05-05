n, a, b = map(int, input().split())
c = list(map(int, input().split()))

ans = a + b

print(c.index(ans) + 1)
