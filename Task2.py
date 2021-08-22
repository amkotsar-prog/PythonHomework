time = int(input('Введите время в с:  '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

