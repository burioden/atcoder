s = input()

flag = 1

for i in range(3):
  if s[i] == s[i+1]:
    flag = 0

print("Good" if flag else "Bad")
