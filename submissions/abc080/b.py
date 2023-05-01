s = input()

num = 0

for i in range(len(s)):
  num += int(s[i])

print("Yes" if int(s)%num == 0 else "No")
