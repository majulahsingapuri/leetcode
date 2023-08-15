class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        left, right, rowLength = 0, len(matrix) - 1, len(matrix[0]) - 1
        def binSearchCol(left, right):
            if right < left:
                return -1
            elif right == left:
                return left
            else:
                mid = (left + right) // 2
                if target < matrix[mid][0]:
                    return binSearchCol(left, mid - 1)
                elif target > matrix[mid][rowLength]:
                    return binSearchCol(mid + 1, right)
                else:
                    return mid

        row = binSearchCol(left, right)
        if row == -1:
            return False

        left, right = 0, rowLength
        def binSearchRow(left, right):
            if right <= left:
                if matrix[row][left] == target:
                    return left
                else:
                    return -1
            else:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return mid
                elif target < matrix[row][mid]:
                    return binSearchRow(left, mid - 1)
                else:
                    return binSearchRow(mid + 1, right)

        return binSearchRow(left, right) != -1