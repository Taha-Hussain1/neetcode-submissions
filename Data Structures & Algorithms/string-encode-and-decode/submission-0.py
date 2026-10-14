class Solution:

    def encode(self, strs: List[str]) -> str:
        sum_word = ""
        for word in strs:
            sum_word = sum_word + "\0" + word
        return sum_word
    def decode(self, s: str) -> List[str]:
        split_string = re.split("\0", s)
        res = []
        for word in split_string[1:]:
            res.append(word)
        return res