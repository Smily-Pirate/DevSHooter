"""def solution(nums, target):
    for i in range(len(nums)):
        if nums[i] - target > 0:
            return i
        else:
            return len(nums)


nums = [1, 3, 5, 6]
target = 2
solution(nums, target)
"""
class Solution:
    def searchInsert(self, nums, target):

        nums.append(target)
        nums.sort()
        for i,j in enumerate(nums):
            if target == j:
                return i


nums = [1, 3, 5, 6]
target = 2
ob1 = Solution()
y = ob1.searchInsert(nums, target)
print(y)

# Other solution
"""
def seatchInsert(self, nums, target):
    try:
        return  nums.index(target)
    except IndexError:
        for index, value in enumerate(nums):
            if value > target:
                return index
        return len(nums)
"""