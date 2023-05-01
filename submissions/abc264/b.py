r,c = map(int, input().split())

#r,cどちらかが1または15の時はblack
#r or c =8の時は偶数=white,奇数=black
#ぱったん、と1/4に折ってみた

if r==15:r=1
if r==14:r=2
if r==13:r=3
if r==12:r=4
if r==11:r=5
if r==10:r=6
if r==9:r=7

if c==15:c=1
if c==14:c=2
if c==13:c=3
if c==12:c=4
if c==11:c=5
if c==10:c=6
if c==9:c=7

ans = [
    ["black","black","black","black","black","black","black"],
    ["black","white","white","white","white","white","white"],
    ["black","white","black","black","black","black","black"],
    ["black","white","black","white","white","white","white"],
    ["black","white","black","white","black","black","black",],
    ["black","white","black","white","black","white","white"],
    ["black","white","black","white","black","white","black"]
]

if r==8:
    if c%2==1:
        print("black")
    else:print("white")
else:print(ans[r-1][c-1])
