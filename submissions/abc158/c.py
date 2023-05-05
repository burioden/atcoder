a,b = map(int,input().split())

for i in range(1,1001):
  if (i*0.08//1) == a and (i*0.1//1) == b:
    print(i)
    exit()

print(-1)
