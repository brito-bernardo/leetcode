class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        if len(words) > 0:
            last_word = words[-1]
            lenght_word = len(last_word)
        return lenght_word