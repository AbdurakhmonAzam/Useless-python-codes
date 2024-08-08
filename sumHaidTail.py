def sum(numbers):
    if len(numbers)==0: #Base Case
        return 0
    else: #Recursive Case
        head=numbers[0]
        tail=numbers[1:]
        return head+sum(tail)
    
nums=[1, 2, 5, 7, 9, 12]
a=sum(nums)
print('The sum of', nums, 'is', a)
nums=[6, 7, 8, 4, 9, 3]
a=sum(nums)
print('The sum of', nums, 'is', a)
nums=[9, 9, 9, 9, 9, 6]
a=sum(nums)
print('The sum of', nums, 'is', a)