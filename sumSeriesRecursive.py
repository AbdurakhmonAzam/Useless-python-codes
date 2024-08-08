def sumSeries(number):
    if number==1:
        return number
    else:
        return number+sumSeries(number-1)
    
print(sumSeries(5))
