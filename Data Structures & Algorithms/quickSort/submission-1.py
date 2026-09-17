# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    def quickSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        pivot = pairs[e]
        ptr = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[ptr] = pairs[ptr], pairs[i]
                ptr += 1
        
        pairs[ptr], pairs[e] = pairs[e], pairs[ptr]

        self.quickSortHelper(pairs, s, ptr - 1)
        self.quickSortHelper(pairs, ptr + 1, e)

        return pairs
