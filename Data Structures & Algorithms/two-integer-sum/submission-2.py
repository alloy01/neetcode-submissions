class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash map 1-pass solution

        hash_map = {}

        for i, num in enumerate(nums):
            req = target - num

            if req in hash_map:
                return [hash_map[req], i]

            hash_map[num] = i