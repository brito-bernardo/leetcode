from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        if not nums:
            return ans

        threshold = len(nums) // 3
        counts = {}  

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for num, count in counts.items():
            if count > threshold:
                ans.append(num)

        return ans
