s = list(input())
a,b = map(int, input().split())

a -= 1
b -= 1

s[a] , s[b] = s[b] , s[a]

out = "".join(s)

print(out)
