class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_dict = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in close_open_dict:
                if stack and stack[-1] == close_open_dict[c]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)
        
        return True if not stack else False
        