def count_move(positions_a, positions_b, m):
    positions_a = int(positions_a)
    positions_b = int(positions_b)
    count = 0

    x = [(1, 2), (-1, 2), (2, -1), (2, 1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]

    for i in x:
        pos_a = positions_a + i[0]
        pos_b = positions_b + i[1]
        if len(m) >= pos_b > 0 < pos_a <= len(m[0]) and m[len(m) - pos_b][pos_a - 1] != " x" and m[len(m) - pos_b][
            pos_a - 1] != " *":
            count += 1
    return count
