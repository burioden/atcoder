n = int(input())

for i in range(1,int(n**0.5+1)):
  if n%i == 0:
    x = i
    y = n//i

print(x+y-2)
