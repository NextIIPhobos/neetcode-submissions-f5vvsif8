class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            delta = target - numbers[left]
            while numbers[right] >= delta:
                if numbers[right] == delta:
                    return [left+1,right+1]
                right -= 1
            left += 1
            

        