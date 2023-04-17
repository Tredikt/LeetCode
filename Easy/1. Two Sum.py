class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        breaking = False
        return_array = []
        for num in range(len(nums)):
            for index_num in nums[nums.index(nums[num]) + 1:]:
                if nums[num] + index_num == target:
                    index = nums.index(nums[num])
                    return_array.append(index)
                    nums[index] = "ad"
                    return_array.append(nums.index(index_num))
                    breaking = True
                    break
            if breaking:
                break
        return return_array