def maze(board, t_r, t_c, row, col, path="", c_r=1, c_c=1):

    if (c_r == t_r) and (c_c == t_c):
        print(path)
        print(board)
        return

    if (c_r not in range(0, row)) or (c_c not in range(0, col)):
        return

    if board[c_r][c_c]:
        return

    board[c_r][c_c] = True
    maze(board, t_r, t_c, row, col, path + "U",  c_r - 1, c_c)
    maze(board, t_r, t_c, row, col, path + "D", c_r + 1, c_c)
    maze(board, t_r, t_c, row, col, path + "L",  c_r, c_c - 1)
    maze(board, t_r, t_c, row, col, path + "R",  c_r, c_c + 1)
    board[c_r][c_c] = False


def maze_li(board, t_r, t_c, row, col, path="", c_r=1, c_c=1):

    if (c_r == t_r) and (c_c == t_c):
        return [path]

    if (c_r not in range(0, row)) or (c_c not in range(0, col)):
        return []

    if board[c_r][c_c]:
        return []

    acc = []
    board[c_r][c_c] = True
    acc.extend(maze_li(board, t_r, t_c, row, col, path + "U",  c_r - 1, c_c))
    acc.extend(maze_li(board, t_r, t_c, row, col, path + "D", c_r + 1, c_c))
    acc.extend(maze_li(board, t_r, t_c, row, col, path + "L",  c_r, c_c - 1))
    acc.extend(maze_li(board, t_r, t_c, row, col, path + "R",  c_r, c_c + 1))
    board[c_r][c_c] = False

    return acc


board = [[False] * 5 for i in range(3)]

li = maze_li(board, 3, 3, 3, 5)

sorted_li = sorted(li, key=lambda item : len(item))

print(sorted_li)