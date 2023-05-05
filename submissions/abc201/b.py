n = int(input())
h_li = []
n_li = []
for i in range(n):
  s,t = input().split()
  n_li.append(s)
  h_li.append(int(t))

x = sorted(h_li)[-2]

for i in range(n):
  if h_li[i] == x:
    print(n_li[i])
    break
