# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, arr, s, e):
        # Base case (arr len of 1)
        if e - s + 1 <= 1:
            return arr

        # Middle index of the array
        m = (s + e) // 2

        # Sort the left half of the array
        self.mergeSortHelper(arr, s, m)

        # Sort the right half of the array
        self.mergeSortHelper(arr, m + 1, e)

        # Merge the sorted halves
        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr, s, m, e):
        # Copy sorted left and right to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        # Declare index pointers for arrays
        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halves into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Loops for the sorted halves with remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1