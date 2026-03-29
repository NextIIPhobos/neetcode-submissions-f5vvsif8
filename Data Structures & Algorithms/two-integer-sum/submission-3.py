class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict_nums:
                return [dict_nums[target-nums[i]], i]
            dict_nums[nums[i]] = i