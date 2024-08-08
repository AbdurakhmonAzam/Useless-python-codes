def factorial(n):
    if n<0:
        return 'Factorial not defined for negative numbers'
    elif n==0:
        return 1
    else:
        result=1
        for i in range(1, n+1):
            result*=i
        return result

number=int(input('Enter a number: '))

factorial_result=factorial(number)
print(f'Factorial of {number} is {factorial_result}')
        