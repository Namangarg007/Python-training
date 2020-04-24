def queens(board, row, n):

    if row == n:
        print("solutin Mil Gya")
        return

    for col in range(0, n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            queens(board, row+1, n)
            board[row][col] = False


def is_safe(board, row, col, n):

    #Up Wards
    for i in range(0, row):
        if board[i][col]:
            return False
    #Left Diagonal
    steps = min(row, col)
    for step in range(1, steps+1):
        if board[row-step][col-step]:
            return False
    #Right Diagonal
    steps = min(row, n-1 - col)
    for step in range(1, steps + 1):
        if board[row - step][col + step]:
            return False

    return True


n = int(input())
board = [[False] * n for i in range(n)]
queens(board, 0, n)