a,b = map(int, input().split())

li = [0]

num = 1

for i in range(2,1000):
  num += i
  li.append(num)

print(abs(b-li[(b-a)-1]))
