def concat(strings):
    if not strings:
        return ''
    else:
       head=strings[0]
       tail=concat(strings[1:])
       return head+tail
    
print(concat(['Hello', 'World']))
 


        
        
