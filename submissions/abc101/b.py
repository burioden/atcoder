n = input()
num = 0

for i in range(len(n)):
  num += int(n[i])

n = int(n)

print("Yes" if n%num==0 else "No")
