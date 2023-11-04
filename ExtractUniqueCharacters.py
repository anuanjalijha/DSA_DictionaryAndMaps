def uniqueChar(s): 
    # Write your code here
    d = dict()
    result =""
    for char in s:
        if char not in d:
            d[char]=1
            result+=char
    
    return result       







# Main 
s=input() 
print(uniqueChar(s))