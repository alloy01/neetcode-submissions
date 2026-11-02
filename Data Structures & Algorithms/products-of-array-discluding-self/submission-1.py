class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force solution

        product = 1
        zero_index = None
        no_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
                no_zero += 1
                continue
            else:
                product *= nums[i]

        if zero_index != None and no_zero < 2:
            ans = [0] * len(nums)
            ans[zero_index] = product
        elif no_zero > 1:
            ans = [0] * len(nums)
        else:
            ans = []
            for num in nums:
                ans.append(product // num)

        return ans