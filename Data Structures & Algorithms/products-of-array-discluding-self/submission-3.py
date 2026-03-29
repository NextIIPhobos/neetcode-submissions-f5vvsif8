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
        for num in nums:
            if num:
                if zero_cnt == 1: res.append(0)
                else: res.append(int(prov/num))
            else:
                res.append(prov)
        return res

