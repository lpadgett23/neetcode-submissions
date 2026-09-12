class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while s[i].isalnum() and s[j].isalnum() and i < j:
            if s[i].lower() != s[j].lower():
                return False
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
        return True