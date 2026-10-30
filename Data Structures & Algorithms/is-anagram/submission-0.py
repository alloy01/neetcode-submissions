class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_array = [0]*26

        for i in range(len(s)):
            hash_array[ord(s[i]) - ord("a")] += 1
        
        for i in range(len(t)):
            hash_array[ord(t[i]) - ord("a")] -= 1

        for i in range(len(hash_array)):
            if hash_array[i] != 0:
                return False
        
        return True