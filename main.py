def starting_position(positions_a, positions_b, m):
    if round(float(positions_a)) != float(positions_a) or round(float(positions_b)) != float(positions_b):
        print("Invalid dimensions!")

    if float(positions_a) < 1 or float(positions_b) < 1 or float(positions_a) > 8 or float(positions_b) > 8:
        print("Invalid dimensions!")

    m[len(m) - int(positions_b)][int(positions_a) - 1] = "X"
    print(" " + "-" * 2 * len(m[0]) + "---")
    x = len(m)
    line_number = []
    for i in range(int(len(m))):
        print(f'{x}| {" ".join(m[i])} |')
        x -= 1
    for i in range(len(m[0])):
        line_number.append(str(i + 1))
    print(" " + "-" * 2 * len(m[0]) + "---")
    z = " ".join(line_number)
    print(f"   {z} ")


def starting_board(board_a, board_b):

    int(board_a)
    int(board_b)

    m = []
    for i in range(int(board_b)):
        m.append([])
        for j in range(int(board_a)):
            m[i].append("_")
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

try:

    positions_a, positions_b = input("Enter the knight's starting position:").split()
    starting_position(positions_a, positions_b, x)
except Exception:
    print("Invalid dimensions!")
