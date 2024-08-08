def sumPowersOf2(n):
    total_sum=0
    for i in range(1, n+1):
        total_sum+=2**i
    return total_sum
print(sumPowersOf2(3))
print(sumPowersOf2(4))

 