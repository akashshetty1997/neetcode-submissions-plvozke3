class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visitedValuesRow = set()
            visitedValuesColumn = set()
            for j in range(9):
                currentRow = board[i][j]
                currentColumn = board[j][i]
                if currentRow != '.':
                    if currentRow in visitedValuesRow:
                        return False
                    else:
                        visitedValuesRow.add(currentRow)

                if currentColumn != '.':
                    if currentColumn in visitedValuesColumn:
                        return False
                    else:
                        visitedValuesColumn.add(currentColumn)

        for boxRow in range(3):
            for boxCol in range(3):
                visitedValuesBox = set()
                for i in range(3):
                    for j in range(3):
                        currentValue = board[boxRow * 3 + i][boxCol * 3 + j]
                        if currentValue != '.':
                            if currentValue in visitedValuesBox:
                                return False
                            else:
                                visitedValuesBox.add(currentValue)

        return True