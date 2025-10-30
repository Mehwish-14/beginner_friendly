def longSubarrSum(nums, k):
    prefix = {0: -1}  # sum -> index
    total = 0
    longest = 0

    for i, n in enumerate(nums):
        total += n

        if total - k in prefix:
            longest = max(longest, i - prefix[total - k])

        if total not in prefix:
            prefix[total] = i

    return longest
