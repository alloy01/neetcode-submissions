class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        my_heap = []

        for num in hash_map.keys():
            heapq.heappush(my_heap, (hash_map[num], num))

            if len(my_heap) > k:
                heapq.heappop(my_heap)

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(my_heap)[1])

        return ans