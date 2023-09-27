class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            words = sentence.split()
            num_words = len(words)
            
            if num_words > maxWords:
                maxWords = num_words

        return maxWords