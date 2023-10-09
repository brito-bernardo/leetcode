from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftBoundary(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def findRightBoundary(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        left_bound = findLeftBoundary(nums, target)
        if left_bound == -1:
            return [-1, -1]

        right_bound = findRightBoundary(nums, target)

        return [left_bound, right_bound]
