def can_attack(piece, position, king_pos, board):
    """
    ตรวจสอบว่าตัวหมากสามารถโจมตี King ได้หรือไม่
    """
    directions = {
        'P': [(-1, -1), (-1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(0, -1), (0, 1), (-1, 0), (1, 0)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    }

    if piece not in directions:
        return False

    for dr, dc in directions[piece]:
        r, c = position
        if piece == 'P':
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            continue

        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != '.':
                break

    return False


def checkmate(board):
    """
    ตรวจสอบว่ามีตัวหมากใดสามารถโจมตี King ได้หรือไม่
    """

    king_pos = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return "Fail"


    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell in "PBRQ":
                if can_attack(cell, (i, j), king_pos, board):
                    return "Success"

    return "Fail"
