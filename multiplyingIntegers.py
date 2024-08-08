def product(numbers):
    if len(numbers) == 0: # BASE CASE
       return 1
    elif len(numbers) == 1:
       return numbers[0]
    else: # RECURSIVE CASE
       head = numbers[0]
       tail = product(numbers[1:])
       return head * tail

print(product([4, 5, 6]))