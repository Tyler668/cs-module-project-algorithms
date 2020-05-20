'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k, arr = []):
    # Your code here
    # maxArray = []
    # max = nums[0]

    # if len(nums) < k:
    #     return arr

    # for i in range(k):
    #     if nums[i] > max:
    #         max = nums[i]
    # arr.append(max)
    # nums.remove(nums[0])
    # sliding_window_max(nums, k, arr)        

    windowMaxes = []
    
    while len(nums) >= k: 
        max = nums[0]
        for i in range(k):
            if nums[i] > max:
                max = nums[i]
        nums.remove(nums[0])
        windowMaxes.append(max)

    return windowMaxes


    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
