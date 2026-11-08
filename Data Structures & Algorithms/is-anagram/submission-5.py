class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if hash_map.get(t[i], 0) == 0:
                return False
            else:
                hash_map[t[i]] -= 1
            
        for val in hash_map.values():
            if val != 0:
                return False
        
        return True