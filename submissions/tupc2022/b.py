n, m, k = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(m)]

now = 0
ride = 0

# 初雪の日
# if d[0][1] - 1 >= k:
  # ride += 1

# 1日目からチェック
for i in range(m):
  day = d[i][0]
  
  if i != m - 1:
    afterDay = d[i + 1][0]
  else:
    afterDay = n + 1

  yuki = d[i][1] - 1
  
  now = now + yuki
  kk = max(0, now - k + 1)

  
  if afterDay - day <= kk:
    ride += (afterDay - day)
  else:
    ride += kk
  
  now = max(0, now - (afterDay - day) + 1)


print(ride)
