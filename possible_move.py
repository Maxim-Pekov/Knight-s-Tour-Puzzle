import count_move


def possible_move(positions_a, positions_b, m):
    positions_a = int(positions_a)
    positions_b = int(positions_b)
    sum_count = 0

    x = [(1, 2), (-1, 2), (2, -1), (2, 1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]

    for i in x:
        pos_a = positions_a + i[0]
        pos_b = positions_b + i[1]
        if len(m) >= pos_b > 0 < pos_a <= len(m[0]) and m[len(m) - pos_b][pos_a - 1] != " *":
            m[len(m) - pos_b][pos_a - 1] = f" {count_move.count_move(pos_a, pos_b, m)}"
            sum_count += int(m[len(m) - pos_b][pos_a - 1])
    return sum_count
