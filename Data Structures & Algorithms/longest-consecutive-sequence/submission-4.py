class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        d = {}
        for num in nums:
            d[num] = 1
            for i in range(1, len(nums)):
                if num + i in nums:
                    d[num] += 1
                    #print(num, num + i)
                else: break
            #print(d)
        return d[max(d, key = d.get)]




