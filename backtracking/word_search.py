def dfs(r, c, i, word, board) -> bool:
    if i == len(word):
        return True
    if (
        r >= len(board) or r < 0 or
        c >= len(board[0]) or c < 0 or
        board[r][c] != word[i]
        or board[r][c]  == '*'
    ):
        return False
        
    board[r][c] = "*"
    result = (
        dfs(r + 1, c, i + 1, word, board) or 
        dfs(r - 1, c, i + 1, word, board) or 
        dfs(r, c + 1, i + 1, word, board) or 
        dfs(r, c - 1, i + 1, word, board)
    )
    board[r][c] = word[i]
    return result    

# Grid m * n, word -> bool
# Returns if word exists in grid
def search(board: list[list[int]], word: str) -> bool:
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j, 0, word, board):
                return True
    return False


def test():
    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))  # True
    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))  # True
    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))  # False    
    print(search([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))  # False


test()