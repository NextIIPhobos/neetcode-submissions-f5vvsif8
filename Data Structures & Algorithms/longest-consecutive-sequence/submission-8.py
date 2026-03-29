class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 in num_set: continue
            current_num = num
            current_len = 1
            while current_num + 1 in num_set:
                current_len += 1
                current_num += 1
            if current_len > max_len: max_len = current_len
        return max_len