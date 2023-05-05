n = int(input())
a = list(map(int,input().split()))

sum = 0

for i in a:
  if i <= 80:
    sum += (80-i)
    
print(sum)
