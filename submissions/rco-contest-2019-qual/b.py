n,m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]

output = []

for i in range(50):
    if a[i][0] < 9:
        time = 9 - a[i][0]
        for _ in range(time):
            output.append(f"1 {i} 0")
        a[i][0] = 9
        m -= time
    if a[0][i] < 9:
        time = 9 - a[0][i]
        for _ in range(time):
            output.append(f"1 0 {i}")
        a[0][i] = 9
        m -= time

output.append("2 0 0")

print(*output, sep="\n")
