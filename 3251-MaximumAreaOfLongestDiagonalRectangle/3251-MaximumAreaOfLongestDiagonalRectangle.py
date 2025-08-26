# Last updated: 8/26/2025, 10:47:53 AM
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Appraoch - Calculate the diagonal in square, and store the biggest diagonal
        # - While updating the biggest diagonal also check for the area. 
        # - If diagonal is same check for the bigger area
        # TC - O()

        long_diag = -1
        max_area = -1

        for l, w in dimensions:
            diag = l*l + w*w
            if diag > long_diag:
                long_diag = diag
                max_area = l*w
            elif diag == long_diag and max_area < l*w:
                max_area = l*w

        return max_area