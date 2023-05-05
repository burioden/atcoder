n = int(input())
t = input()

now_l = ["east","south","west","north"]
now_p = [1,-1,-1,1]

now = now_l[0]
x = 0
y = 0

for i in range(n):
  if t[i] == "S":
    if now == now_l[0]:
      x += now_p[0]
    elif now == now_l[1]:
      y += now_p[1]
    elif now == now_l[2]:
      x += now_p[2]
    else:
      y += now_p[3]
  else:
    if now == now_l[0]:
      now = now_l[1]
    elif now == now_l[1]:
      now = now_l[2]
    elif now == now_l[2]:
      now = now_l[3]
    else:
      now = now_l[0]

print(x,y)
