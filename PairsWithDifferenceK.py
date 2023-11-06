def printPairDiffK(l, k):
    m = dict()
    ans = 0
    for num in l:
        if num+k in m:
            ans += m[num+k]
        if k!=0 and num-k in m:
            ans += m[num-k]

        # Update map        
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
            

    return ans
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))