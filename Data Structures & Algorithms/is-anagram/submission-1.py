class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        hash_table_t = {}
        for i in range(len(s)):
            if s[i] in hash_table_s:
                hash_table_s[s[i]] += 1
            else:
                hash_table_s[s[i]] = 1
        
        for x in range(len(t)):
            if t[x] in hash_table_t:
                hash_table_t[t[x]] += 1
            else:
                hash_table_t[t[x]] = 1
        
        return hash_table_t == hash_table_s