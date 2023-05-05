n,m = map(int,input().split())
a = list(input().split())
b = set(input().split())

for i in range(n):
  if a[i] in b:
    print("Yes")
  else:
    print('No')
