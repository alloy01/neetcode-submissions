class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        answer = False 
        hash_map = {}

        for i in range(len(nums)):
            if hash_map.get(nums[i], 0) == 0:
                hash_map[nums[i]] = 1
            else:
                answer = True
                break

        return answer
                    