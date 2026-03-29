class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        max_len = 0
        
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_len = 1
                
                while current_num + 1 in nums:
                    current_num += 1
                    current_len += 1
                
                max_len = max(max_len, current_len)
        
        return max_len