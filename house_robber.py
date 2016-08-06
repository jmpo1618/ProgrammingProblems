class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not len(nums):
                return 0
            if len(nums) == 1:
                return nums[0]
            results = []
            results.append(nums[0])
            results.append(max(results[0], nums[1]))
            for i in range(2, len(nums)):
                results.append(max(results[i - 2] + nums[i], results[i-1]))
            return results[-1]
