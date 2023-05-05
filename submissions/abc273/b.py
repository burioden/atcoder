x,k = map(int,input().split())

for i in range(1,k+1):
  x = round(x+1,-i)
  
print(x)
