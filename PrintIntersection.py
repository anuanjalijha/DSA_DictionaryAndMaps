def printIntersection(arr1, n1, arr2, n2) :
    # Create a hash map to store the elements from the first array
    hashmap = {}
    
    # Populate the hash map with elements from the first array
    for num in arr1:
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1    
    
    # Create a list to store the intersection elements
    intersection = []
    
    # Iterate through the second array
    for num in arr2:
        # If the element is in the hash map and its count is greater than 0, it's an intersection element
        if num in hashmap and hashmap[num] > 0:
            intersection.append(num)
            # Decrement the count in the hash map to avoid duplicates
            hashmap[num] -= 1
    
    for num in intersection:
        print(num)

