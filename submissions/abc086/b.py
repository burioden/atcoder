a,b = input().split()

num = int(a+b)

flag = 0

for i in range(1,num):
  if i*i == num:
    flag = 1

print("Yes" if flag else "No")
