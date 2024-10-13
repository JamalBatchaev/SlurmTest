import random

a=random.randint(1, 100)

b=0

for i in range(1, 9):
        print(f'Попытка №{i}:')
        b=int(input())
        if a==b:
            print('Вы угадали!')
            break
        else:
            print('Вы не угадали!')
            if b>a:
                print('Загаданное число меньше указанного вами!')
            else:
                print('Загаданное число больше указанного вами!')
            
else:
    print('Вы проиграли...')    

