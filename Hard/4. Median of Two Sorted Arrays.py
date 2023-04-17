class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merged_array = sorted(nums1)

        length = len(merged_array)
        if length % 2 == 1:
            return merged_array[length // 2]

        else:
            return (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2