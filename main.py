def starting_position(positions_a, positions_b, m):
    int(positions_a), int(positions_b)
    assert float(positions_a) > 0 and float(positions_b) > 0, "а и б должно быть больше 0"

    m[len(m) - int(positions_b)][int(positions_a) - 1] = "X" if len(m) < 10 else " x"

        # add "-----------------" over the table
    print(" ---" + "-" * 2 * len(m[0])) if len(m) < 10 else print("  ---" + "-" * 3 * len(m[0]))

    x = len(m)
    line_number = []
    for i in range(int(len(m))):
        print(f' {x}| {" ".join(m[i])} |') if x < 10 and len(m) > 9 else print(f'{x}| {" ".join(m[i])} |')
        x -= 1

    for i in range(len(m[0])):

        # add line "01 02 03 04..." under the table
        line_number.append(" " + str(i + 1)) if len(m) >= 10 and i < 9 else line_number.append(str(i + 1))

        # add "-----------------" under the table
    print(" ---" + "-" * 2 * len(m[0])) if len(m) < 10 else print("  ---" + "-" * 3 * len(m[0]))

    z = " ".join(line_number)
    print(f"   {z} ") if len(m) < 10 else print(f"    {z} ")


def starting_board(board_a, board_b):
    assert int(board_a) < 100 and int(board_b) < 100  # check board size (1 - 99)
    assert int(board_a) > 0 and int(board_b) > 0
    m = []
    for i in range(int(board_b)):
        m.append([])
        for j in range(int(board_a)):
            m[i].append("_") if int(board_b) < 10 and int(board_a) < 10 else m[i].append("__")
    return m


def ask_board_size():
    try:
        board_a, board_b = input("Enter your board dimensions:").split()
        global x
        x = starting_board(board_a, board_b)
    except Exception:
        print("Invalid dimensions!")
        ask_board_size()
    return x


x = ask_board_size()


def ask_first_position():
    try:
        positions_a, positions_b = input("Enter the knight's starting position:").split()
        starting_position(positions_a, positions_b, x)
    except Exception:
        print("Invalid dimensions!")
        ask_first_position()


ask_first_position()
