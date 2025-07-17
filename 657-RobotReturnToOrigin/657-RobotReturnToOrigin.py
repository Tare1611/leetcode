# Last updated: 7/16/2025, 8:14:36 PM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #  Brute force approach : use for loop to traverse through the input string. Assign opposite values to U&D and R&L
        # TC - O(n), SC - O(1)

        # x = y = 0
        # for move in moves:
        #     if move == 'U':
        #         y += 1
        #     elif move == 'D':
        #         y -= 1
        #     elif move == 'R':
        #         x += 1
        #     elif move == 'L':
        #         x -= 1
        #     else:
        #         print("Invalid Move")
        # return x == 0 and y == 0

        #  Other approach use a counter to check if the number of moves in opposite direction are same or not.
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')