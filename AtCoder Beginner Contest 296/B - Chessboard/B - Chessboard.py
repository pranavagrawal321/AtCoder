chess_board = []
for i in range(8):
    a = input()
    chess_board.append(a)
    if "*" in a:
        print(chr(97+a.index("*")) + str(8-i))