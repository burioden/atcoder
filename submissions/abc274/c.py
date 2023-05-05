n = int(input())
a = list(map(int,input().split()))

ans = [0]

for i in a:
  ans += [ans[i-1]+1]*2

print(*ans,sep="\n")
