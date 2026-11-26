class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        if n == 1:
            return triplets[0] == target
        x, y, z = 0, 0, 0
        for i in range(n):
            a, b, c = triplets[i]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if (x != target[0] and a == target[0]) or (y != target[1] and b == target[1]) or (z != target[2] and c == target[2]):
                x = max(x, a)
                y = max(y, b)
                z = max(z, c)
        return x == target[0] and y == target[1] and z == target[2]    