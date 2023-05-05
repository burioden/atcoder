n = list(input())

num = 0
for i in n:
    num += int(i)
    
print('Yes' if num % 9 == 0 else 'No')
