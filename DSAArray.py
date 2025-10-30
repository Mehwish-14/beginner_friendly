def longest_subarray_sum(nums, k):
    """
    Returns the length of the longest subarray with sum equal to k.

    Args:
        nums (List[int]): List of integers.
        k (int): Target sum.

    Returns:
        int: Length of the longest subarray whose sum is equal to k.
    """
    prefix_sum_index = {0: -1}  # Maps prefix_sum -> earliest index
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if there exists a prefix_sum such that current_sum - prefix_sum = k
        if (prefix_sum - k) in prefix_sum_index:
            max_length = max(max_length, i - prefix_sum_index[prefix_sum - k])

        # Store prefix_sum if not seen before (to ensure longest possible subarray)
        if prefix_sum not in prefix_sum_index:
            prefix_sum_index[prefix_sum] = i

    return max_length
