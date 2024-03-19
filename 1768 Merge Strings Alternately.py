class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = list(word1)
        word2 = list(word2)
        final_str = ""
        for letter in word1:
            final_str += letter
            if word2:
                final_str += word2[0]
                word2.pop(0)

        for letter in word2:
            final_str += letter

        return final_str
