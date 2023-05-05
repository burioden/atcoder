import itertools

s,k = input().split()
k = int(k)

ans = itertools.permutations(s,len(s))
ans = sorted(set(ans))

print(*list(ans[k-1]),sep="")
