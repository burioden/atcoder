import collections

n = int(input())
a = list(map(int,input().split()))

aa = collections.Counter(a)
ans = aa.most_common()[-1][0]

print(ans)
