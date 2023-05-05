n = int(input())
a = sorted(list(map(int, input().split())))
t = int(input())

ans = set()

for i in a:
  ans.add(i // t)

print(len(ans))
