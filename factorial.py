def factorial(number):
    if number==1:
        #Base Case
        return 1
    else:
        #Recursive Case
        return number*factorial(number-1)
print(factorial(6))