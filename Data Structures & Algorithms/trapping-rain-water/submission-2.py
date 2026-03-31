import numpy as np

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        matrix = np.zeros(max(height)*len(height))
        matrix = matrix.reshape((max(height), -1))
        for i, h in enumerate(height):
            for j in range(h):
                matrix[j,i] = 1
        print(matrix)
        print(matrix.shape)
        for i in range(matrix.shape[0]):
            left = 0
            right = matrix.shape[1]-1
            for j in range(0, matrix.shape[1]):
                if matrix[i,j] == 1: 
                    left = j
                    break
                
            for j in range(matrix.shape[1]-1,-1,-1):
                if matrix[i, j] == 1: 
                    right = j
                    break
                
            for j in range(left+1, right):
                if matrix[i,j] == 0: matrix[i,j] =2
                    
        print(matrix) 
        number_of_5 = np.count_nonzero(matrix == 2)
        return int(number_of_5)
        
