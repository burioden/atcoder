n = int(input())
li = [int(input()) for _ in range(n)]

print(len(li) - len(set(li)))
