class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matching_pair = {}

        for i, num in enumerate(nums):
            if num in matching_pair: # target-num found!
                return [matching_pair[num], i] # return index of found pair (earlier), and num (later)
            matching_pair[target-num] = i # if u found target-num -> here is index of num



        