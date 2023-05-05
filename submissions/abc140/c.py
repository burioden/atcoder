n = int(input())
b = list(map(int,input().split()))

a = [b[0]]
for i in range(1,n-1):
  a.extend([min(b[i-1],b[i])])

a.extend([b[-1]])

print(sum(a))
