'''
距離をとって、どっちが最小か？を出す
A1→B1→A2→B2... 2を掛けて距離を出す
xかけて1進む、yかけて2進む minを出す
A→Bには必ず行くからxは足す
'''

a,b,x,y = map(int,input().split())

mya = min(2*x,y)
nya = abs(2*b+1-2*a)

print(int(nya/2)*mya+x)
