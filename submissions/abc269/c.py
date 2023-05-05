n = int(input())
ans = [n]

while ans[-1] > 0:
  ans.append((ans[-1]-1)&n)

print(*ans[::-1],sep="\n")
