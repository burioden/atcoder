import heapq

n,m = map(int,input().split())
# この下の2つって一気に書ける方法あるのかな…？
a = list(map(int,input().split()))
a = [-i for i in a]

heapq.heapify(a)

for i in range(m):
  x = -heapq.heappop(a)
  heapq.heappush(a,-(x//2))
  
print(-sum(a))
