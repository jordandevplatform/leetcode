class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = [[-1, -1, [-1]]]
        
        i, j, c = 0, 0, 0
        
        while i <= 8 and j <= 8:
		
		#Skip is cell is a number
            if board[i][j] != '.':
                c += 1
                i = c // 9
                j = c % 9
                continue

			#If we are are at an already explored cell, we just have to subsitute the cell with one of the possible values, or if none available, backtrack.
            if i == stack[-1][0] and j == stack[-1][1]:
			
				#If no possible values, then backtrack
                if stack[-1][2] == []:
                    stack.pop()
                    i, j = stack[-1][0], stack[-1][1]
                    board[i][j] = "."
                    c = (i * 9) + j
                    continue
                
				#Else substitute the cell with one of its possible values and remove the stubstituted value from the stack
                board[i][j] = stack[-1][2].pop()
                c += 1
                i = c // 9
                j = c % 9
                continue
            
            
			#For an unexplored cell, find out all possible values
            possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
			
			#Check for row and column
            for a in range(0, 9):
                if board[i][a] in possible:
                    possible.pop(possible.index(board[i][a]))
                if board[a][j] in possible:
                    possible.pop(possible.index(board[a][j]))
                
			#Check for box
            for a in range((i//3)*3, (i//3)*3 + 3):
                for b in range((j//3)*3, (j//3)*3 + 3):
                    if board[a][b] in possible:
                        possible.pop(possible.index(board[a][b]))
            
			#Push the possible state onto the stack
            stack.append([i, j, possible])