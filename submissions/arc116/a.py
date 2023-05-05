'''
奇数:偶数の約数は存在しないからodd
偶数:わる2した結果が奇数のものはsame
    他はeven
'''
tora = int(input())
for inu in range(tora):
  neko = int(input())
  if neko%2 == 1:
    print('Odd')
  elif (neko//2)%2 == 1:
    print('Same')
  else:
    print('Even')
  
