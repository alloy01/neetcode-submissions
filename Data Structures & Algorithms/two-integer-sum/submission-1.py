class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash map 2-pass solution

        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            req = target - nums[i]
            if (hash_map.get(req) != None) and (i != hash_map.get(req)):
                return [i, hash_map.get(req)]