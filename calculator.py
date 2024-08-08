while True:
    operation=input('Enter operation(+, -, *, /, **): ')

    if operation.lower()=='Exit':
        print('Exiting the calculator, goodbye!')
        break
    
    a=float(input('First number: '))
    b=float(input('Second number: '))

    if operation=='+':
        result=a+b
    elif operation=='-':
        result=a-b
    elif operation=='*':
        result=a*b
    elif operation=='/':
        result=a/b
    elif operation=='**':
        result=a**b
    else:
        result='Error, please try again'

    print(f'Result: {result}')
    


