class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            if greatest < temp:
                greatest = temp
        return arr