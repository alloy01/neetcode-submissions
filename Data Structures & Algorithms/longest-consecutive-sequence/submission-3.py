class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_num = 1
        num = 1
        nums.sort()

        for i in range(0, (len(nums) - 1)):

            if (nums[i] == nums[i + 1]):
                continue
            elif (nums[i] + 1) == nums[i + 1]:
                num += 1
            else:
                num = 1

            max_num = max(max_num, num)
        
        if len(nums) < 2:
            return len(nums)

        return max_num