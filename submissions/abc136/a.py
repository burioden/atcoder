a, b, c = map(int, input().split())

ans = c -  (a - b)

print(max(0, ans))
