class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for p1 in range (len(nums)):
            for p2 in range (p1 + 1, len(nums)):
                if nums[p1] + nums[p2] == target:
                    return [p1, p2]
            

nums = [5,11,2,15, 7]
target = 26

solution=Solution()
print(solution.twoSum(nums=nums, target=target))