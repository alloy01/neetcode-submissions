class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        arr = []

        for num, count in hash_map.items():
            arr.append([count, num])
    
        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])

        return ans