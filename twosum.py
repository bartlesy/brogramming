# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in seen:
                return i, seen[diff]
            seen[x] = i
        return


if __name__ == "__main__":
    sln = Solution()
    print(sln.twoSum([2, 7, 11, 15], 9))
    print(sln.twoSum([6, 3, 5, 5, 11, 15], 10))
