s = list(input())
a,b = map(int,input().split())

A = s[a-1]
B = s[b-1]

s[a-1] = B
s[b-1] = A

print(*s,sep="")
