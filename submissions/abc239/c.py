a,b,c,d = map(int, input().split())

# 2点間距離の関数すごい とっておく
def df(A,B,C,D):
  return (A-C) ** 2 + (B-D) ** 2

def f(x1,y1,x2,y2):
  for i in range(x1-2,x1+3):
    for j in range(y1-2,y1+3):
      if df(i,j,x1,y1) == df(i,j,x2,y2) == 5:
        return 'Yes'
  return 'No'

print(f(a,b,c,d))
