class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdigit() or c[1:].isdigit(): 
                if c[0] == '-': stack.append(-1 * int(c[1:]))
                else: stack.append(int(c))
            elif c == '+':
                cache_num = stack[-2] + stack[-1]
                stack.pop()
                stack[-1] = cache_num
            elif c == '-':
                cache_num = stack[-2] - stack[-1]
                stack.pop()
                stack[-1] = cache_num
            elif c == '*':
                cache_num = int(stack[-2] * stack[-1])
                stack.pop()
                stack[-1] = cache_num
            elif c == '/':
                cache_num = int(stack[-2] / stack[-1])
                stack.pop()
                stack[-1] = cache_num
        return stack[-1]
            
            


        