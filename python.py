# What to analysis an unknown temperature
Temperature = ''
#Whats to loop to be able to ask the user various temperature until they quit
while True:
# Ask the user to input their temperature to know the condition    
    value = input('What is your temperature? (if unknown or done type quit) ')
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

num+=1