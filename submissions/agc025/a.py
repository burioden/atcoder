n = int(input())
N = list(map(int,str(n)))
if n%10==0:
  print(10)
else:
  print(sum(N))
