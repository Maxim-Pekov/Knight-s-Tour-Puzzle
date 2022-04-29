import count_move
import print_board

count_list = [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7"]


def check_next_move(position_a, position_b, m):
    position_a = int(position_a)
    position_b = int(position_b)
    try:
        assert m[len(m) - position_b][position_a - 1] in count_list
    except Exception:
        print("Invalid move!", end=' ')
        return False
    return True


def next_move(position_a, position_b, m):
    position_a = int(position_a)
    position_b = int(position_b)
    count = 0

    x = [(1, 2), (-1, 2), (2, -1), (2, 1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]

    if m[len(m) - int(position_b)][int(position_a) - 1] == " 0":
        return 1

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] in count_list:
                m[i][j] = "__"

    m[len(m) - int(position_b)][int(position_a) - 1] = " x"

    for i in x:
        pos_a = position_a + i[0]
        pos_b = position_b + i[1]
        if len(m) >= pos_b > 0 < pos_a <= len(m[0]) and m[len(m) - pos_b][pos_a - 1] != " *":
            m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a, pos_b, m)}"

    if print_board.print_board(position_a, position_b, m) == 0:
        print("No more possible moves!")
        return 1
