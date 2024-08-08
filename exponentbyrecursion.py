def exponentByRecursion(a, n):
    if n==1:
        #Base Case
        return a
    elif n %2==0:
        #Recursive Case (even)
        result=exponentByRecursion(a, n//2)
        return result*result
    elif n %2==1:
        #Recursive Case (odd)
        result=exponentByRecursion(a, n//2)
        return result*result*a
    
print(exponentByRecursion(4, 2))
print(exponentByRecursion(3, 4))
print(exponentByRecursion(5, 5))