class Solution:
    def prod(self, nums):
        prod = 1
        for num in nums:
            prod *= num
        return prod

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            left, right = nums[:i], nums[i+1:]
            # print(left, right)
            # print(self.prod(left)*self.prod(right))
            res.append(self.prod(left)*self.prod(right))

        return res