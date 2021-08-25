number = int(input('Введите целое положительное число: '))
largest_num = 0
while number > 0:
    remain = number % 10
    if remain > largest_num:
        largest_num = remain
    number //= 10
print(largest_num)