class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_t = {}
        d_s = {}
        l_s1 = len(s1)
        for c in s1:
            d_t[c] = d_t.get(c,0) +1
        left = 0
        for right in range(len(s2)):
            d_s[s2[right]] = d_s.get(s2[right], 0) + 1
            if right - left == l_s1:
                d_s[s2[left]] -= 1
                left += 1
            matches = sum(k in d_s and d_t[k] == d_s[k] for k in d_t)
            if right - left == l_s1 - 1 and matches == len(d_t):
                return True
        return False

                
            
