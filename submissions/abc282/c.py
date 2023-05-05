n = int(input())
s = list(input())

cnt = 0
for i in range(n):
  if s[i] == '"':
    cnt += 1
  elif s[i] == ',' and cnt%2 == 0:
    s[i] = '.'

print(*s,sep="")
