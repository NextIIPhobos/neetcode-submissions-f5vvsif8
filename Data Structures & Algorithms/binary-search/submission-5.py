class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target: return start
        elif nums[end] == target: return end
        while end - start > 1:
            mid = (end + start) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        return -1