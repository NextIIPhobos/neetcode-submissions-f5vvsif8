class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        l_i = 0
        r_i= length - 1 
        while l_i < length and r_i >= 0 and l_i != r_i:
            while l_i < length and not s[l_i].lower().isalnum():
                l_i += 1
            while r_i >= 0 and not s[r_i].lower().isalnum():
                r_i -= 1
            if l_i < length and r_i >= 0:
                if s[l_i].lower() != s[r_i].lower():
                    return False
            l_i += 1
            r_i -= 1
        return True
            
            