n = int(input())
d = sorted(list(map(int,input().split())))

print(min(d[(n//2):]) - max(d[:(n//2)]))
