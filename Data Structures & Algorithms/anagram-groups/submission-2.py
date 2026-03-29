class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dict_res = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in dict_res:
                dict_res[''.join(sorted(strs[i]))].append(i)
            else:
                dict_res[''.join(sorted(strs[i]))] = [i]
        for s, ind in dict_res.items():
            strs_list = []
            for i in ind:
                strs_list.append(strs[i])
            result.append(strs_list)
        return result