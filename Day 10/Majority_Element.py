class Solution:
    def majorityElement(self, nums):
        majority_candidate = 0
        count = 0
        
        for num in nums:
            if count == 0:
                majority_candidate = num
            count += 1 if num == majority_candidate else -1
        
        return majority_candidate
