class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def different_digits(digits):
            if 0 <= digits <= 9:
                return str(digits)
            else:
                return chr(ord('A') + digits - 10)



        for base in range(2, n -1 ):
            result = ""
            temp_num = n

            while temp_num > 0:
                remainder = temp_num % base
                result = different_digits(remainder) + result
                temp_num //= base
            if result != result[::-1]:
                return False
        
        return True
        