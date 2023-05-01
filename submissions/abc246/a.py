x, y = zip(*[map(int, input().split()) for _ in range(3)])

X = x[0] ^ x[1] ^ x[2]
Y = y[0] ^ y[1] ^ y[2]

print(X, Y)
