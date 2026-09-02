class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            candidate = prefix + char

            if all(s.startswith(candidate) for s in strs):
                prefix = candidate
            else:
                break

        return prefix            
                

            

