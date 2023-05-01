n = int(input())
a,b = map(int, input().split())
p = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in p:
  if i <= a:
    cnt1 += 1
    # print("f")
  elif a < i and i <= b:
    cnt2 += 1
    # print("e")
  else:
    cnt3 += 1
    # print("d")

print(min(cnt1,cnt2,cnt3))
