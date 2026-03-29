class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prov, zero_cnt = 1, 0
        ln = len(nums)
        for num in nums:
            if num:
                prov *= num
            else:
              zero_cnt += 1
    
        if zero_cnt > 1: return [0] * ln

        res = []
        for i, c in enumerate(nums):
            if zero_cnt: res.append(0) if c else res.append(prov)
            else: res.append(int(prov/c))
        return res

