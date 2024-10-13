value = int(input())
 
count = 0
for i in range(value):
    for _ in range(i + 1):
        count += 1
        print (count, end=' ')
    print()