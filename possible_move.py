import count_move
def possible_move(positions_a, positions_b, m):
    positions_a = int(positions_a)
    positions_b = int(positions_b)

    pos_a = positions_a + 1
    pos_b = positions_b + 2
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a, pos_b, m)}"


    pos_a = positions_a - 1
    pos_b = positions_b + 2
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    pos_a = positions_a + 2
    pos_b = positions_b - 1
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"

    pos_a = positions_a + 2
    pos_b = positions_b + 1
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    pos_a = positions_a + 1
    pos_b = positions_b - 2
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    pos_a = positions_a - 1
    pos_b = positions_b - 2
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    pos_a = positions_a - 2
    pos_b = positions_b + 1
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    pos_a = positions_a - 2
    pos_b = positions_b - 1
    if pos_b > 0 < pos_a and pos_b <= len(m) and pos_a <= len(m[0]):
        m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a,pos_b, m)}"


    return m
