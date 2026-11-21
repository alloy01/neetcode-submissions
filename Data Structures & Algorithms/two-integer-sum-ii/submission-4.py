class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            to_find = target - numbers[i]
            x = i + 1  # Start after 'i' to avoid reusing the same index
            y = len(numbers) - 1

            while x <= y:  # Use <= so the single remaining element is checked
                mid = (x + y) // 2
                if numbers[mid] == to_find:
                    return [i + 1, mid + 1]
                elif numbers[mid] > to_find:
                    y = mid - 1  # Narrow search to the left half
                else:
                    x = mid + 1  # Narrow search to the right half
