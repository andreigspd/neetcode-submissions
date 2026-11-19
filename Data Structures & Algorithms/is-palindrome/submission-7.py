class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        left = 0
        right = len(s) - 1
        while left <= right:
            if left <= right and not s[left].isalnum():
                left += 1
                continue
                
            if left <= right and not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True