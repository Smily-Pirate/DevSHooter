# Given an array of integers nums and an integer target, return indices of the
# Two numbers such that they add up to target.
from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :return: List[int]
        """
        required = {}  # returns list of array
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


input_list = [2, 8, 12, 15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))

# Algorithm
"""To solve this, we will loop through each element of the array. So follow there steps to solve this.
     - Define one map to hold the result called res
     - For index i in range 0 to n - 1 (Where n is the number of elements in the array)
           - if target - A[i] is present in res
               - return res[target - A[i]] and i as indices
           - Otherwise put i into the res as res[A[i]] -= i"""


# Method 2
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# The Dictionary Solution
"""
for each number in list of numbers:
    result = subtract number from target number
    look for result in the dictionary (instant lookup)
    if found:
        :return index of number and index of dictionary lookup reault
    else:
        add number to dictionary as key with value being the index
"""