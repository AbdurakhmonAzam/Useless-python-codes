def bill_split(amount, friends):
    total_bill=amount*1.20
    amount_per_friend=total_bill/friends
    return round(amount_per_friend, 2)
   
amount=float(input('The bill: '))
friends=int(input('Number of friends: '))

amount_each=bill_split(amount, friends)
print(f'Each friend pays: ${amount_each}')

