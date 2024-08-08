def sumPowersOf2(n):
    if n==1:
        return 2
    #Base Case
    else:
        return 2**n+sumPowersOf2(n-1)
    #Recursive Case

print(sumPowersOf2(3))
print(sumPowersOf2(5))
        
        
   