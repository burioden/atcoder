n = int(input())
s = list(input())
S = []
for i in s:
  if 90 < ord(i)+n:
    S.append(chr(ord(i)+n-26))
  else:
    S.append(chr(ord(i)+n))
    

print(*S,sep="")
