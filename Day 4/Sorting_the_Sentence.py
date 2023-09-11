class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [""] * len(words)

        for word in words:
            position = int(word[-1]) - 1
            ans[position] = word[:-1]
        return ' '.join(ans)
        