from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for str in strs:
            k= "".join(sorted(str))
            res[k].append(str)

        return list(res.values())
