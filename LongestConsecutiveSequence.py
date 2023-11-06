def lengthOfLongestConsecutiveSequence(arr, n):
    mx = 0
    
    # To store the length of current consecutive Sequence.
    count = 0
    
    # To store all the unique elements of array.
    sett = set()
    
    for element in arr:
        sett.add(element)
        
    for element in arr:
        
        previousConsecutiveElement=element-1
        
        if(not previousConsecutiveElement in sett):
            
            # Element is the first value of consecutive sequence.
            j = element
            
            while j in sett:
                
                # The next consecutive element by will be j + 1.
                j += 1
            
            # Update maximum length of consecutive subsequence.
            mx = max(mx , j-element)
     
    return mx
