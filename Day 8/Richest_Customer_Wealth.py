class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for customer in accounts:
            ans = 0
            for bank in customer:
                ans += bank
            if max_value < ans:
                max_value = ans
                
            
        return max_value