s=list(input())
n=len(s)

if s[0] == "0":
 s.insert(0,1)
 n+=1
 
cnt = 0
for i in range(n):
 if i%2 == 1 and s[i] == "1":
  cnt+=1
 elif i%2 == 0 and s[i] == "0":
  cnt+=1

print(cnt)
