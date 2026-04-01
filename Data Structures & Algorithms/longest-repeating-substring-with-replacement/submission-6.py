class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #d = {chr(n): 0 for n in range(ord('A'),ord('Z')+1) }
        d = {}
        l,r = 0,0
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            f = max(d.values())
            length = r - l + 1
            if length - f > k:
                d[s[l]] -= 1
                l += 1
            r+=1
        return r-l
                    
