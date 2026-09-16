class Solution:
    def isValid(self, s: str) -> bool:
        freq = {}
        freq["{"] = "}"
        freq["("] = ")"
        freq["["] = "]"
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif not stack or freq[stack.pop()] != char:
                return False
        return not stack