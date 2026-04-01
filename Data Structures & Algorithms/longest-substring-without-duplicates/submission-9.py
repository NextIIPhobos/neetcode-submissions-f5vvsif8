class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        delta = 0
        l = 0
        r = 1
        sub_set=set(s[l])
        m = len(sub_set)
        while r < len(s):
            if s[r] in sub_set:
                #m = max(m,len(sub_set))
                l += 1
                r = l + 1
                sub_set=set(s[l])
            else:
                sub_set.add(s[r])
                r += 1
            
            ##print(sub_set)
            m = max(m,len(sub_set))
        return m
            

        