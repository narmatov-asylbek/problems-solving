package main

import "fmt"

func exist(board [][]byte, word string) bool {
	m := len(board)
	n := len(board[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(board, word, i, j, 0) == true {
				return true
			}
		}
	}
	return false
}

func dfs(board [][]byte, word string, i, j, k int) bool {
	if k == len(word) {
		return true
	}
	if i < 0 || j < 0 || i == len(board) || j == len(board[0]) || word[k] != board[i][j] {
		return false
	}
	board[i][j] = '#'
	res := dfs(board, word, i+1, j, k+1) || dfs(board, word, i-1, j, k+1) || dfs(board, word, i, j+1, k+1) || dfs(board, word, i, j-1, k+1)
	board[i][j] = word[k]
	return res
}

func main() {
	fmt.Println("Fuck you")
}
