class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_repeat = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for i in nums1:
            if i in nums2:
                nums_repeat.append(i)
        
        return nums_repeat