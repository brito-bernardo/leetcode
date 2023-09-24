class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_let = []
        for i in s:
            if i.isalnum():  
                s_let.append(i.lower())  
        return s_let == s_let[::-1] 
