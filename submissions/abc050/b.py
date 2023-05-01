n = int(input())
q = list(map(int, input().split()))
m = int(input())
drink = []
for _ in range(m):
    a, b = map(int, input().split())
    drink.append([a, b])

for i in range(m):
    print(sum(q)+drink[i][1]-q[drink[i][0]-1])
