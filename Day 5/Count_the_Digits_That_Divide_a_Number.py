class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        num_string = str(num)

        for s in num_string:
            digit = int(s)
            if digit != 0 and num % digit == 0:
                count+= 1

        return count