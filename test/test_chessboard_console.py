def draw_chessboard():
    chessboard = [['' for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                chessboard[i][j] = '⬜'
            else:
                chessboard[i][j] = '⬛'

    for row in chessboard:
        print(''.join(row))

draw_chessboard()