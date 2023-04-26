def findMin(self, nums: List[int]) -> int:

    smallest_val = float("inf")

    l = 0
    r = len(nums) - 1
    

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < smallest_val:
            smallest_val = nums[mid]
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1
        
        
    return smallest_val
