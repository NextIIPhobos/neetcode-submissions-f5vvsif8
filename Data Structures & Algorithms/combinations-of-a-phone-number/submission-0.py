class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        
        d = {1: (), 
        2: ('a', 'b', 'c'),
        3: ('d', 'e', 'f'),
        4: ('g','h','i'),
        5: ('j','k','l'),
        6: ('m','n','o'),
        7: ('p','q','r','s'),
        8: ('t','u','v'),
        9: ('w','x','y','z')}

        res = []
        
        def dfs(i,sub):
            if i == len(digits):
                res.append(sub)
                return
            
            int_i = int(digits[i])
            for l in range(len(d[int_i])):
                dfs(i+1,sub + d[int_i][l])

        dfs(0,'')
        return res
        