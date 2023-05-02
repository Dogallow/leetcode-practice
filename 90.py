def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr_arr = []
        res = []

        def dfs(index):

            if index > len(nums) - 1:
                res.append(curr_arr.copy())
                return

            curr_arr.append(nums[index])
            dfs(index + 1)

            curr_arr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1)
        
        dfs(0)

        return res


    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     dupe_set = set()
    #     curr_arr = []
    #     res = []

    #     def dfs(index):

    #         if index > len(nums) - 1:
    #             sorted_arr = curr_arr.copy()
    #             if not tuple(sorted_arr) in dupe_set:
    #                 res.append(sorted_arr)
    #                 set_arr = tuple(sorted_arr)
    #                 dupe_set.add(set_arr)

    #             return

    #         curr_arr.append(nums[index])
    #         dfs(index + 1)

    #         curr_arr.pop()
    #         dfs(index + 1)
        
    #     dfs(0)

    #     return res
