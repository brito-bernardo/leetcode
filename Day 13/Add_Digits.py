class Solution:
    def addDigits(self, num: int) -> int:
        def separateDigits(n: int) -> int:
            tempSum = 0
            while n > 0:
                digit = n % 10
                tempSum += digit
                n //= 10
            return tempSum

        while num > 9:
            num = separateDigits(num)

        return num