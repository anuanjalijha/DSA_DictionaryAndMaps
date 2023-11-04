def pairSum0(l,n):
    # Variable to store the count of pairs.
    count = 0
    
    # Hash-map to store frequency of each element.
    mp = {}
    
    for i in range(n):
        
        if l[i] in mp:
            mp[l[i]] += 1
        
        
        else:
            mp[l[i]] = 1
            
    # Iterating the hash-map.
    for i in mp:
        
        curKey = i
        
        # Checking if curKey is not equal to 0.
        # Also checking if -curKey exists in the hash-map.
        if curKey != 0 and ((-1)*i in mp):
            
            # Multiplying frequencies and adding them to count.
            count += mp[-i] * mp[i]
            
            
    # Handling the border case when array element is equal to 0.
    if 0 in mp:
        f = mp[0]
        
        # Multiplying f and f-1 and adding it to count.
        count += f * (f - 1)
        
    return count //2
            
            
        
             

