Ax,Ay,Bx,By = map(int, input().split())

Xsa = Bx - Ax
Ysa = By - Ay

Cx = Bx - Ysa
Cy = By + Xsa
Dx = Cx - Xsa
Dy = Cy - Ysa

print(Cx,Cy,Dx,Dy)
