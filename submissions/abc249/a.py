a,b,c,d,e,f,x = map(int, input().split())

ta = 0
ao = 0

# どうして「time%(a+c) < a」で、進んでる秒数が判定できるのかわからない
# time = 0,1,2...x秒 という認識が間違っている？？
for time in range(x):
  if time%(a+c) < a:
    ta += b
  if time%(d+f) < d:
    ao += e

if ta > ao:
  print("Takahashi")
elif ta < ao:
  print("Aoki")
else:
  print("Draw")
