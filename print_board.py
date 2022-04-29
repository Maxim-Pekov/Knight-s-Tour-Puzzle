import possible_move


def print_board(position_a, position_b, m):
    possible_move.possible_move(position_a, position_b, m)

    print(" ---" + "-" * 3 * len(m[0])) if len(m) < 10 else print(
        "  ---" + "-" * 3 * len(m[0]))

    x = len(m)
    line_number = []
    for i in range(int(len(m))):
        print(f' {x}| {" ".join(m[i])} |') if x < 10 and len(m) > 9 else print(
            f'{x}| {" ".join(m[i])} |')
        x -= 1

    for i in range(len(m[0])):
        line_number.append(" " + str(i + 1)) if i < 9 else line_number.append(str(i + 1))

    print(" ---" + "-" * 3 * len(m[0])) if len(m) < 10 else print(
        "  ---" + "-" * 3 * len(m[0]))

    z = " ".join(line_number)
    print(f"   {z} ") if len(m) < 10 else print(f"    {z} ")
    print()
