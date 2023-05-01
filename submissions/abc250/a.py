h, w = map(int, input().split())
r, c = map(int, input().split())

ans = 4

if r == 1 or r == h:
    ans -= 1
if c == 1 or c == w:
    ans -= 1
if h == 1:
    ans -= 1
if w == 1:
    ans -= 1

print(ans)
