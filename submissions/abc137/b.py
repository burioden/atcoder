k,x = map(int, input().split())

start = x-(k-1)
end = x+k

for i in range(start,end):
  print(i,end=" ")
