def findSubstringIterative(needle, haystack):
    i=0
    while i<len(haystack):
        if haystack[i:i+len(needle)]==needle:
            return i #Needle Found
        i=i+1
    return -1 #Needle NOT Found

def findSubstringRecursive(needle, haystack, i=0):
    if i>=len(haystack):
        return -1 #Base Case (Needle not found.)
    
    if haystack[i:i+len(needle)]==needle:
        return i #Base Case (Needle found.)
    else:
        #Recursive Case
        return findSubstringRecursive(needle, haystack, i+1)

print(findSubstringIterative('cat', 'My cat Zophie'))
print(findSubstringRecursive('cat', 'My cat Zophie'))