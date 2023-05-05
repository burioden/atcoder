n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(set(a + b))
z = {v:i + 1 for i, v in enumerate(c)}

print(*list(map(lambda v: z[v], a)))
print(*list(map(lambda v: z[v], b)))
