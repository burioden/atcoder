s = list(input())
n = int(input())
li = []
for i in range(n):
  x,y = map(int, input().split())
  X = s[x-1:y][::-1]
  s[x-1:y] = X

print(*s,sep="")
