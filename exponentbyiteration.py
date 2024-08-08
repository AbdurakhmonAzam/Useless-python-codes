def exponentByIteration(a, n):
    result=1
    for i in range(n):
        result *=a
    return result

print(exponentByIteration(10, 6))
print(exponentByIteration(5, 7))
print(exponentByIteration(100, 100))