h1,h2,h3,w1,w2,w3 = map(int,input().split())

# x  x  H1  →  h1
# x  x  H2  →  h2
# W1 W2 W3  →  h3(H3)
# ↓  ↓  ↓
# w1  w2 w3

# xの部分を i,j,k,l 4つの数字で動かす
cnt = 0
for i in range(1,29):
  for j in range(1,29):
    for k in range(1,29):
      for l in range(1,29):
        H1 = h1-(i+j)
        H2 = h2-(k+l)
        W1 = w1-(i+k)
        W2 = w2-(j+l)
        W3 = w3-(H1+H2)
        H3 = W1+W2+W3
        cnt += (min(H1,H2,H3,W1,W2,W3) > 0 and h3 == H3)

print(cnt)
