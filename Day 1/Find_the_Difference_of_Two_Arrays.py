class Solution:


    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_norepeat = []
        nums2_norepeat = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:

            if i not in nums2:
                nums1_norepeat.append(i)

        for i in nums2:
            if i not in nums1:
                nums2_norepeat.append(i)


        return [nums1_norepeat,nums2_norepeat]