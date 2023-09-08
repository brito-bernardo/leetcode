class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dictionary = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        previous_number = 0

        for c in s:
            current_number = roman_dictionary[c]

            if current_number > previous_number:
                total += current_number - 2 * previous_number
            else:
                total += current_number
            previous_number = current_number
        
        return total
            