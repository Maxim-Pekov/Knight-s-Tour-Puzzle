def starting_position(a, b):
    if round(float(a)) != float(a) or round(float(b)) != float(b):
        print("Invalid dimensions!")

    if float(a) < 1 or float(b) < 1 or float(a) > 8 or float(b) > 8:
        print("Invalid dimensions!")

    m = []
    for i in range(8):
        m.append([])
        for j in range(8):
            m[i].append("_")
    m[8 - int(b)][int(a) - 1] = "X"
    print(" --------------------\n"
          f"8| {m[0][0]} {m[0][1]} {m[0][2]} {m[0][3]} {m[0][4]} {m[0][5]} {m[0][6]} {m[0][7]} |\n"
          f"7| {m[1][0]} {m[1][1]} {m[1][2]} {m[1][3]} {m[1][4]} {m[1][5]} {m[1][6]} {m[1][7]} |\n"
          f"6| {m[2][0]} {m[2][1]} {m[2][2]} {m[2][3]} {m[2][4]} {m[2][5]} {m[2][6]} {m[2][7]} |\n"
          f"5| {m[3][0]} {m[3][1]} {m[3][2]} {m[3][3]} {m[3][4]} {m[3][5]} {m[3][6]} {m[3][7]} |\n"
          f"4| {m[4][0]} {m[4][1]} {m[4][2]} {m[4][3]} {m[4][4]} {m[4][5]} {m[4][6]} {m[4][7]} |\n"
          f"3| {m[5][0]} {m[5][1]} {m[5][2]} {m[5][3]} {m[5][4]} {m[5][5]} {m[5][6]} {m[5][7]} |\n"
          f"2| {m[6][0]} {m[6][1]} {m[6][2]} {m[6][3]} {m[6][4]} {m[6][5]} {m[6][6]} {m[6][7]} |\n"
          f"1| {m[7][0]} {m[7][1]} {m[7][2]} {m[7][3]} {m[7][4]} {m[7][5]} {m[7][6]} {m[7][7]} |\n"
          " -------------------\n"
          "   1 2 3 4 5 6 7 8 ")


print("Enter the knight's starting position:")
try:
    a, b = input().split()
    starting_position(a, b)
except Exception:
    print("Invalid dimensions!")

