def ackermann(m, n, identation=None):
    if identation is None:
        identation = 0
    print('%sackermann(%s, %s)' %(' ' * identation, m, n))

    if m == 0:
        #Base Case
        return n + 1
    elif m > 0 and n == 0:
        #Recursive Case
        return ackermann(m - 1, 1, identation + 1)
    elif m > 0 and n > 0:
        #Recursive Case
        return ackermann(m - 1, ackermann(m, n - 1, identation + 1), identation + 1)
    
print('Starting with m=1, n=1:')
print(ackermann(1, 1))
print('Starting with m=2, n=3:')
print(ackermann(5, 6))