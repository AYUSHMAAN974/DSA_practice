def Longest_Substring(N, array, s):
    lp = 0
    max_len = 0
    curr_sum = 0
    
    for rp in range(N):
        curr_sum += array[rp]
        
        while curr_sum > s and lp <= rp:
            curr_sum -= array[lp]
            lp += 1
        
        if curr_sum == s:
            length = rp - lp + 1
            max_len = max(max_len, length)
            
    return max_len

print(Longest_Substring(7, [1, 2, 3, 1, 1, 1, 1], 3))  
