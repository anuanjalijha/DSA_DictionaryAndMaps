def mostFrequent(arr,n):
    freq = dict()
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1    

    # Insert all elements in Hash.
    
    # find the max frequency
    max_count = 0
    most_frequent_num = None

    for num, count in freq.items():
        if count > max_count:
            max_count = count
            most_frequent_num = num

    return most_frequent_num
# Get the number of integers from the user
num_of_integers = int(input())

# Get the list of integers from the user
arr = []
for i in range(num_of_integers):
    num = int(input())
    arr.append(num)
