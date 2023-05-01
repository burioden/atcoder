n, q = map(int, input().split())
L = []
for i in range(n):
    list = input().split()
    L.append(list)
Q = []
for i in range(q):
    a, b = map(int, input().split())
    Q.append([a, b])

for i in range(q):
    print(L[Q[i][0]-1][Q[i][1]])
