n = int(input())
li = [int(input()) for _ in range(n)]

li = sorted(set(li))

print(li[-2])
