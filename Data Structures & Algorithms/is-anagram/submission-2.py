class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for i in range(len(s)):
            if hash_map.get(s[i], 0) != 0:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        
        for i in range(len(t)):
            if hash_map.get(t[i], 0) == 0:
                return False
            else:
                hash_map[t[i]] -= 1

        for value in hash_map.values():
            if value != 0:
                return False
            
        
        return True