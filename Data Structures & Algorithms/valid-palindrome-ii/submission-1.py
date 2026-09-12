class Solution:
    def validPalindrome(self, s: str) -> bool:
        def test_pal(substring):
            return substring == substring[::-1]

        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return test_pal(s[l+1:r+1]) or test_pal(s[l:r])
            l+=1
            r-=1

        return True


