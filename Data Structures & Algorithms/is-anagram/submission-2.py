class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        for x in s:
            count_s[x] = 1 + count_s.get(x, 0)
        for y in t:
            count_t[y] = 1 + count_t.get(y, 0)
        
        if count_s == count_t:
            return True
        else:
            return False

