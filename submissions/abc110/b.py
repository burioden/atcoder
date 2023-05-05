n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

X.append(x)
Y.append(y)

X.sort()
Y.sort()

if max(X) < min(Y):
  print("No War")
else:
  print("War")
