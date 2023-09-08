class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_repeat = []

        for i in nums1:
            if i in nums2 and nums_repeat.count(i) < nums2.count(i):
                nums_repeat.append(i)
        
        return nums_repeat