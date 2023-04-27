def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    max_consecutive = 0
    for num in nums:
        if num == 1:
            count += 1
            max_consecutive = max(count, max_consecutive)
        else:
            count = 0
    return max_consecutive
