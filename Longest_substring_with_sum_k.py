def Longest_Subarray_With_Sum_K(array, k):
    prefix_map = {}    
    curr_sum = 0
    max_len = 0
    start_index = -1    

    for i in range(len(array)):
        curr_sum += array[i]

        if curr_sum == k:
            max_len = i + 1
            start_index = 0

        if (curr_sum - k) in prefix_map:
            prev_index = prefix_map[curr_sum - k]
            length = i - prev_index
            if length > max_len:
                max_len = length
                start_index = prev_index + 1

        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i

    if max_len == 0:
        print("No subarray found with sum =", k)
    else:
        print("Longest subarray with sum", k, "is:")
        print(array[start_index : start_index + max_len])
        print("Length:", max_len)

    return max_len


Longest_Subarray_With_Sum_K([1, -1, 5, -2, 1, 1, -2, 4], 3)
