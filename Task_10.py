# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

num = int(input('Введите кол-во монет: '))
resh = 0
orel = 0
coins  = []

for i in range(num):
    random_number = round(random.uniform(0, 1))
    coins.append(random_number)

    if coins[i] <= 0:
        resh += 1
        
    elif coins[i] >= 1:
        orel += 1
       
    
print(f'Выполи монетки: {coins}')
print(f'Выполо решек {resh}')
print(f'Выполо орлов {orel}')
if resh == 0 or resh == num:
    print('Монетки лежат одной стороной!')
elif resh == orel:
    print(f'Переверните любые монеты.')
    print(f'Нужно перевернуть {resh}')

elif resh < orel:
    print(f'Нужно перевернуть монетки лежащие решкой вверх {resh}')

else:
    print(f'Нужно перевернуть монеты лежащие орлом вверх {orel}')