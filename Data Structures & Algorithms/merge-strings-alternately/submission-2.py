class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minword_totalchars=min(len(word1),len(word2))
        # longerword = max(len(word1),len(word2)) # not actually needed, an empty slot in slice will return the whole end of the string in python
        res=""
        word1.split()
        word2.split()

        i=0

        for i in range(minword_totalchars):
            res += word1[i]
            res += word2[i]

            i+=1
        
        if len(word1) > len(word2):
            res += word1[minword_totalchars:]
        else:
            res += word2[minword_totalchars:]
  

        return res

