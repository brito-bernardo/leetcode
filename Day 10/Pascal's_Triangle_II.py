class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            prev = 1
            for j in range(1, i):
                curr = row[j]
                row[j] += prev
                prev = curr

        return row
