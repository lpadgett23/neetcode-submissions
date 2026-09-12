class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = []
        w1, w2 = len(word1), len(word2)

        for i in range(max(w1, w2)):
            if i < w1:
                chars.append(word1[i])
            if i < w2:
                chars.append(word2[i])
  
        return "".join(chars)

