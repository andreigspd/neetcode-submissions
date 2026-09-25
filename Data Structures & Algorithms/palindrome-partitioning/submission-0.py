class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def is_palindrome(sub: str):
            return sub == sub[::-1]
        def bkt(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for i in range(start + 1, len(s) + 1):
                part = s[start : i]
                if is_palindrome(part):
                    path.append(part)
                    bkt(i, path)
                    path.pop()
        bkt(0, [])
        return result