n = int(input())
# 先頭に0を2つ入れることにより、インデックス番号を変更
li = [0,0]+list(map(int, input().split()))

crr = n
cnt = 0

# リストを遡っていく
while crr!=1:
  cnt += 1
  crr = li[crr]
  # print("人" + str(n) + "の" + str(cnt) + "代前は、人" + str(crr))

print(cnt)
