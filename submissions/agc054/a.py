n = int(input())
s = input()

if s[0] != s[n-1]:
  print(1)
  exit()

for i in range(n-1):
    if s[0] != s[i]:
      if s[0] != s[i+1]:
        print(2)
        exit()

print(-1)
