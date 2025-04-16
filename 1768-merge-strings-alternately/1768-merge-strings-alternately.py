class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        merged = []

        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append the remaining characters from word1 or word2
        if i < len(word1):
            merged.extend(word1[i:])
        if j < len(word2):
            merged.extend(word2[j:])

        return ''.join(merged)
