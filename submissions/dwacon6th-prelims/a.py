n = int(input())

title = []
time = []

for i in range(n):
  s,t = input().split()
  t = int(t)
  time.append(t)
  title.append(s)


x = input()

sleep = title.index(x)
print(sum(time[sleep+1:]))
