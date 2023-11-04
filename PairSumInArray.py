def pair_sum(arr, target):
    freq = dict()
    ans = 0

    for num in arr:
        expect = target - num
        ans += freq.get(expect, 0)
        if freq.get(num, 0):
            freq[num] += 1
        else:
            freq[num] = 1

    return ans