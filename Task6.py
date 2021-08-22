distance = int(input('Введите результат спортсмена в первый день: '))
distance_fin = int(input('Введите общий результат спортсмена: '))
day = 1
while distance <= distance_fin:
    day += 1
    distance *= 1.1
else:
    print(f'Спортсмен достиг результата на {day} день')


