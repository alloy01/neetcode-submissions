class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using nested loops

        for i in range(len(nums)):
            req = target - nums[i]
            for j in range(i + 1, len(nums)):   
                if nums[j] == req:
                    return [i, j]