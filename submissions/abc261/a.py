a,b,c,d = map(int, input().split())

l1 = []
l2 = []

for i in range(a,b):
    l1.append(i)
for i in range(c,d):
    l2.append(i)

l1_l2_and = set(l1) & set(l2)

l1_l2_and_list = list(l1_l2_and)

print(len(l1_l2_and))
