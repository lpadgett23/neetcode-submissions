class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minword_totalchars=min(len(word1),len(word2))
        longerword = max(len(word1),len(word2))
        res=""
        word1.split()
        word2.split()

        i=0

        for i in range(minword_totalchars):
            res=res+res.join(word1[i])
            res=res+res.join(word2[i])

            i+=1
        
        if word1 > word2:
            res=res+word1[minword_totalchars:longerword]
        else:
            res=res+word2[minword_totalchars:longerword]
  

        return res

