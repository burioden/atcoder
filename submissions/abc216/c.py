n = int(input())

ans = []
while n > 0:
  if n%2 == 1:
    n -= 1
    ans.append("A")
  else:
    n //= 2
    ans.append("B")
    
print(*ans[::-1],sep="")
