class Solution:
    def validPalindrome(self, s: str) -> bool:
        stackleft = []
        stackright = []
        l = 0
        r = len(s)-1

        while l <= r:
            stackleft.append(s[l])
            stackright.append(s[r])
            l+=1
            r-=1

        i=max(len(stackleft)-1, len(stackright)-1)

        for i in range(len(stackleft), -1, -1):  # i'm not sure if i need to set i above or if -1 and -1 is enough to go from top down in a stack
            l_char = stackleft.pop(i)
            r_char = stackright.pop(i)
            if l_char != r_char:
                # it needs a rule to skip up to one time but exit if twice?
                    # it would need to increment one or the other then compare them again?
                    return False

                # increment either(or both?) l_char or r_char down by one?

        
        return True