number = int(input('Введите целое положительное число: '))
while number // 10 > 1:
    a = number % 10
    number = number // 10
    b = number % 10
    if a > b:
        a = a
    else:
        a = b
print(f'{a} - самая большая цифра в  данном числе')



