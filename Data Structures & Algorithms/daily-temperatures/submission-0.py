class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indexes_stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack or (temperatures[i] <= stack[-1]):
                stack.append(temperatures[i])
                indexes_stack.append(i)
            else:
                while stack and temperatures[i] > stack[-1]:
                    stack.pop()
                    j = indexes_stack.pop()
                    output[j] = i-j
                stack.append(temperatures[i])
                indexes_stack.append(i)
        return output
        