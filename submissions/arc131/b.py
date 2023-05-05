h, w = map(int, input().split())
g = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '.':
            g[i][j] = 0
        else:
            g[i][j] = int(s[j])
    
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

for i in range(h):
    for j in range(w):
        # 「.」をみつけたら
        if g[i][j] == 0:
            used = [0,0,0,0,0,0]
            # 周りの4マスを調べるチェックループへ
            for k in range(4):
                nx = j + DX[k]
                ny = i + DY[k]
                if 0 <= ny < h and 0 <= nx < w:
                    used[g[ny][nx]] = 1
            for k in range(1,6):
                if used[k] == 0:
                    g[i][j] = k
                    break

for i in g:
    print(*i,sep='')
