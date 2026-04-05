class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            cache = []
            for c in s:
                if c == '(':
                    cache.append(c)
                elif not cache and c == ')':
                    return False
                else:
                    cache.pop()
            return not cache

        sub = ''

        def dfs(i,sub):
            #nonlocal sub
            if len(sub) == 2*n:
                if valid(sub):
                    res.append(sub[::])
                return

            dfs(i+1,sub + '(')
            dfs(i+1,sub + ')')
        
        dfs(0,sub)
        return res      