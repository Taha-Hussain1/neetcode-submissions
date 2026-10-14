class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l, r = 0, 1
        longest = 0
        while r < len(s):
            temp_l = l
            while temp_l < r:
                if s[temp_l] == s[r]:
                    l = temp_l + 1
                    break   
                temp_l += 1
            current_length = r - l + 1
            longest = max(longest, current_length)   
            r += 1
        return longest