class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = "".join(filter(str.isalnum, s)).lower()
        for index, char in enumerate(filtered_string):
            if char != filtered_string[len(filtered_string) - index - 1]:
                return False
        return True