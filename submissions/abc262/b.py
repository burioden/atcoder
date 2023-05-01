n,m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

cnt = 0

for i in range(n):
	for j in range(i+1,n):
		for l in range(j+1,n):
			if graph[i][j] == 1 and graph[l][i] == 1 and graph[j][l] == 1:
				cnt += 1

print(cnt)

#2重め、3重めループでi+1とj+1が行われている理由がわからない…
