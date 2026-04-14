class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        patch = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": 
                    continue
                box_idx = (i//3)*3+j//3
                if num in row[i] or num in col[j] or num in patch[box_idx]:
                    return False 
                row[i].append(num)
                col[j].append(num)
                patch[box_idx].append(num)
        return True
        
        