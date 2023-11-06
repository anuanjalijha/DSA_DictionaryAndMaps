from collections import OrderedDict
def subsetSum(l):
    # Map to store the previous sums
    presum = OrderedDict()

    sum = 0  # Initialize the sum of elements
    maxLen = 0  # Initialize result
    n = len(l)

    # Traverse through the given array
    for i in range(n):
        # Add current element to sum
        sum += l[i]

        if (l[i] == 0 and maxLen == 0):
            maxLen = 1
        if sum == 0:
            maxLen = i + 1

        # Look for this sum in Hash table
        if (sum in presum):
            # If this sum is seen before, then update maxLen
            maxLen = max(maxLen, i - presum.get(sum))

        else:
            # Else insert this sum with index in hash table
            presum[sum] = i

    return maxLen

    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))