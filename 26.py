class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = None
        index = 0

        # For my way of thinking here. A While loop was essential to be able to alter the index variable. In a for loop the progression of the index value was circumvented by python.
        while index < len(nums):
            # Another note is being aware that 0 is a False value in conditionals. So, that can prevent you from entering code blocks.
            if tmp or tmp == 0:
                # Check if the previous value is equal to the current value. If so, remove it.
                if tmp == nums[index]:
                    nums.remove(nums[index])
                    # And we want to adjust our index to stay consistent with the positions and length of our current nums array.
                    # The only way we dont want to decrement our index is if our index is already at the beginning aka 0. This could happen if we have more than 2 duplicates at the start of our array.
                    if index != 0:
                        index -= 1
            # Use the tmp variable to store the previous value
            if index < len(nums):
                tmp = nums[index]
            
            index += 1

        return len(nums)
