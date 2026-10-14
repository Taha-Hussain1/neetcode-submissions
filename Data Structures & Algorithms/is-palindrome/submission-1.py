class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""
        stripped = ""
        for letter in (s):
            if letter.isalnum():
                copy = letter.lower() + copy
                stripped = stripped + letter.lower()
        return copy == stripped