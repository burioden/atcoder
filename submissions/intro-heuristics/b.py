d = int(input())
c = list(map(int,input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input())-1 for _ in range(d)]

day = [0 for i in range(26)]

manzoku = 0
for i,m in enumerate(t):
  manzoku += s[i][m]
  day[m] = i+1
  for j in range(26):
    manzoku -= c[j]*(i+1 - day[j])
  print(manzoku)
    
    
#ダメだったコード
# day = [-1 for i in range(26)]

# manzoku = [0]*d
# for i in range(d):
#   manzoku[i] = s[i][t[i]]

# for i in range(1, len(manzoku)):
#   manzoku[i] += manzoku[i-1]

# print(manzoku)

# for i,m in enumerate(t):
#   if day[m] == -1:
#     last = 0
#     day[m] = i
#     print("1回目",day)
#   else:
#     last = day[m]
#     day[m] = i
#     print("2回目",day)
#   manzoku[i] = manzoku[i] - (c[t[i]]*(d - last)) # ここが誤読してる d-ではない

# print(manzoku)
