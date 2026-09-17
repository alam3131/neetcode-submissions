# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
        
    def quickSortHelper(self, arr, s, e):
        if s >= e:
            return arr

        pivot = arr[e].key
        left = s
        
        for i in range(s, e):
            if arr[i].key < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        
        arr[e], arr[left] = arr[left], arr[e]

        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)

        return arr