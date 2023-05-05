n,m = map(int,input().split())
a = set(list(map(int,input().split())) + [n])

ans = []
inner = []

for i in range(1,n+1):
  if i not in a:
    if len(inner) > 0:
      inner.append(i)
      inner = sorted(inner,reverse=1)
      ans.extend(inner)
      inner = []
    else:
      ans.append(i)
  else:
    inner.append(i)

inner = sorted(inner,reverse=1)

ans.extend(inner)

print(*ans,sep=' ')
