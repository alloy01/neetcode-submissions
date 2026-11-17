class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ("".join([char for char in s if char.isalnum()])).lower()
        n = len(clean_str)
        x = 0
        y = n - 1

        for i in range(0, (n // 2)):
            if clean_str[x] != clean_str[y]:
                return False
            else:
                x += 1
                y -= 1
            
        return True