class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_t = {}
        d_s = {}
        l_s1 = len(s1)
        for c in s1:
            d_t[c] = d_t.get(c,0) +1
        left = 0
        #print(d_t)
        #print()
        for right in range(len(s2)):
            d_s[s2[right]] = d_s.get(s2[right], 0) + 1
            if right - left == l_s1:
                d_s[s2[left]] -= 1
                left += 1
            equals = sum(k in d_s and d_t[k] == d_s[k] for k in d_t)
            if right - left == l_s1 - 1 and equals == len(d_t):
                return True
          ##  if left > 20:
          #      print(left, right, len(s1), equals)
           #     print(d_t)
           #     print(d_s)
           #     print(equals)
           #     print(right - left == l_s1 - 1, equals == len(d_t))
           #     print()
        return False

                
            
