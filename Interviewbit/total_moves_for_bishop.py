class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # left_bottom + left_top + right_bottom + right_top
        return min((8-A), (B-1))+min((A-1), (B-1))+min((8-A), (8-B))+min((A-1), (8-B))
    

class Solution:
    def solve(self, A, B):
        col_left = B - 1
        col_right = 8 - B
        row_up = A - 1
        row_down = 8 - A
        ans = min(col_left, row_up) + min(col_left, row_down) + min(col_right, row_up) + min(col_right, row_down)
        return ans