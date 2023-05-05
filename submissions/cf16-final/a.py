h,w = map(int,input().split())
snuke = [list(input().split()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if snuke[i][j] == 'snuke':
            print(chr(j+65),i+1,sep='')
