s = input()
t = input()

ans = []

for i in range(len(s)):
  x = ord(t[i]) - ord(s[i])
  ans.append(x%26)

print('Yes' if len(set(ans)) == 1 else 'No')
