class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1 
        
        for i in reversed(range(len(digits))):
            temp_sum = digits[i] + carry
            carry = temp_sum // 10 
            ans.insert(0, temp_sum % 10)  

        if carry:
            ans.insert(0, carry)
        
        return ans