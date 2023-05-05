h,w = map(int,input().split())
a = [list(input()) for _ in range(h)]

a = [i for i in a if "#" in set(i)]
a = list(zip(*a))
a = [i for i in a if "#" in set(i)]
a = list(zip(*a))

for i in a:
  print(*i,sep="")
