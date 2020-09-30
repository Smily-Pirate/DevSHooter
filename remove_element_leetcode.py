class Solution(object):
    def removeElement(self, nums, val):

        for x in nums[:]:
            if x == val:
                nums.remove(x)

        return len(nums)


test = Solution()
num1 = [0,1,2,2,3,0,4,2]
print(test.removeElement(num1, 2))

print(num1[:])

# Related to -> [:].
def func(value):
    print(id(value), "before change")
    value[:] = value[::-1]
    print(id(value), "after [:]")
    value = value[::-1]
    print(id(value), "after regular assign")

a = [0,1,2,2,3,0,4,2]
print(id(a), "original")
func(a)