    windowMaxes = []
    
    while len(nums) >= k: 
        max = nums[0]
        for i in range(k):
            if nums[i] > max:
                max = nums[i]
        nums.remove(nums[0])
        windowMaxes.append(max)

    return windowMaxes