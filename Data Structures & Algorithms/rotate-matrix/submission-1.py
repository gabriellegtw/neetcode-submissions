class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):

                topLeft = matrix[l][l + i]

                # Shift bottom left to top left
                matrix[l][l + i] = matrix[r - i][l]

                # Shift bottom right to bottom left
                matrix[r - i][l] = matrix[r][r - i]

                # Shift the top right to bottom right
                matrix[r][r - i] = matrix[l + i][r]

                # Shift top left to top right
                matrix[l + i][r] = topLeft

            l += 1
            r -= 1 
        