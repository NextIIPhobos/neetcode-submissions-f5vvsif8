class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_0 = len(matrix[0])
        c_length = len(matrix) * len_0
        if (c_length == 1 and matrix[0][0] == target) or matrix[0][0] == target or matrix[-1][-1] == target: 
            return True
        c_left = 0
        c_right = c_length-1
        
        while c_right - c_left > 1:            
            mid = (c_left + c_right) // 2
            mid_m = mid // len_0
            mid_v = mid - mid_m * len_0
            mid_num = matrix[mid_m][mid_v]
            print(c_left,c_right)
            print(mid, mid_m, mid_v, mid_num)
            if mid_num == target: return True
            if target > mid_num:
                c_left = mid
            else:
                c_right = mid

        return False
