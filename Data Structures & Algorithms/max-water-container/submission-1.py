class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = 0
        right = length - 1
        max_square = 0
        while left < right:
            print(heights[left], heights[right])
            width = right - left
            if heights[left] < heights[right]:
                square = heights[left] * width
            else:
                square = heights[right] * width
            if square > max_square: max_square = square
            d_l_width = heights[left] - width
            d_r_width = heights[right] - width
            if d_l_width < d_r_width:
                left += 1
            elif d_l_width > d_r_width:
                right -= 1
            else:
                left+=1
        return max_square
