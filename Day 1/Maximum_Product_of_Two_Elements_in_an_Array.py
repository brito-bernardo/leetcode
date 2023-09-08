class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_number = 0
        number = 0
        for i,j in enumerate(nums):
            for k,z in enumerate(nums):
                if i != k:
                    number = (j-1) * (z-1)
                    if final_number < number:
                        final_number = number
        return final_number