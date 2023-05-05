h, a = map(int, input().split())

n = h // a
m = h % a

print(n + (m > 0))
