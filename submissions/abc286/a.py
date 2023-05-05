n,a,b,c,d = map(int, input().split())
A = list(map(int,input().split()))

if a > 1:
  print(*A[:a-1],*A[c-1:d],*A[b:c-1],*A[a-1:b],*A[d:])
else:
  print(*A[c-1:d],*A[b:c-1],*A[a-1:b],*A[d:])
