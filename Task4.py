number_init = int(input('Введите целое положительное число: '))
max_digit = 0
number = number_init

while number // 10 > 0:
    digit = number % 10
    if digit >= max_digit:
        max_digit = digit

    number = number // 10
print(f'{max_digit} - самая большая цифра в  данном числе')
