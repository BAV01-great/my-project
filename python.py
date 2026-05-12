Temperature = ''
while True:
    value = input('What is your temperature: ')
    if value == 'quit':
        print('Program ends')
        break
    Temperature = int(value)
    if Temperature <= 0:
        print(float(Temperature))
        print('Freezing')
    elif  1<= Temperature <=15:
        print(float(Temperature))
        print('Cold')
    elif  16 <= Temperature <=25:
        print(float(Temperature))
        print('Warm')
    elif 26<= Temperature <=35:
        print(float(Temperature))
        print('Hot')
    else:
        print(float(Temperature))
        print('Dangerous')

