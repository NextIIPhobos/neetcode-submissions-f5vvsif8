class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {}
        for i in range(len(nums)):
            res_dict[nums[i]] = 1 + res_dict.get(nums[i],0)
        result = []
        for i in range(k):
            result.append(max(res_dict, key = res_dict.get))
            del res_dict[max(res_dict, key = res_dict.get)]
        return result
        