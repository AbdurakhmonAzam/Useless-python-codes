def fibonacci(nthNumber):
    a, b=1, 1
    print('a=%s, b=%s' %(a, b))
    for i in range(2, nthNumber):
        a, b=b, a+b #Get the next fibonacci number.
        print('a=%s, b=%s' %(a, b))
    return a
print(fibonacci(10))