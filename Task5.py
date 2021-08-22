cash_flow = int(input('Введите значение выручки (рублей): '))
costs = int(input('Введите значение издержек (рублей): '))
profit = cash_flow - costs
if profit > 0:
    print(f'фирма работает с прибылью {profit} (рублей)')
    efficiency = profit / cash_flow
    print(f'{efficiency } - рентабельность выручки')
    employ_number = int(input('Введите количество сотрудников: '))
    normal_profit = profit / employ_number
    print(f'{normal_profit} - прибыль фирмы в расчёте на одного сотрудника')
else:
    print(f'фирма работает с убытком: {abs(profit)} (рублей)')
