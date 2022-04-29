import print_board
import next_moves


class ChessBoard():
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.board = []
        self.position_a = 1
        self.position_b = 1
        self.count_move = 0

    def check_board_size(self):
        try:
            assert int(self.side_a) < 100 and int(self.side_b) < 100
            assert int(self.side_a) > 0 and int(self.side_b) > 0
        except Exception:
            print("Invalid dimensions!")
            return False
        return True

    def create_board(self):
        while True:
            try:
                self.side_a, self.side_b = input("Enter your board dimensions:").split()
            except Exception:
                print("Invalid dimensions!")
                continue
            if self.check_board_size():
                break

        for i in range(int(self.side_b)):
            self.board.append([])
            for j in range(int(self.side_a)):
                self.board[i].append("__")
        while True:
            try:
                self.position_a, self.position_b = input("Enter the knight's starting position:").split()
            except Exception:
                print("invalid dimensions!")
                continue
            if self.check_position():
                break
        self.board[len(self.board) - int(self.position_b)][int(self.position_a) - 1] = " x"

    def check_position(self):
        try:
            assert int(self.position_a) <= int(self.side_a) and int(self.position_b) <= int(self.side_b)
            assert float(self.position_a) > 0 and float(self.position_b) > 0
        except Exception:
            print("Invalid move!")
            return False
        return True

    def next_move1(self):

        while True:
            try:
                a, b = input("Enter your next move:").split()
                assert int(a) <= int(self.side_a) and int(b) <= int(self.side_b)
                assert float(a) > 0 and float(b) > 0

            except Exception:
                print("Invalid move!", end=' ')
                continue
            self.board[len(self.board) - int(self.position_b)][int(self.position_a) - 1] = " *"
            self.position_a, self.position_b = a, b
            if self.check_position():
                if next_moves.check_next_move(self.position_a, self.position_b, self.board):
                    break
        if next_moves.next_move(self.position_a, self.position_b, board_start.board) == 1:
            return 1


board_start = ChessBoard(1, 1)
board_start.create_board()
print_board.print_board(board_start.position_a, board_start.position_b, board_start.board)

while (int(board_start.side_b) * int(board_start.side_a)) > board_start.count_move:
    board_start.count_move += 1
    z = board_start.next_move1()
    if (int(board_start.side_b) * int(board_start.side_a)) == board_start.count_move + 1:
        print("What a great tour! Congratulations!")
        break
    if z == 1:
        print("No more possible moves!")
        print(f"Your knight visited {board_start.count_move + 1} squares!")
        break
