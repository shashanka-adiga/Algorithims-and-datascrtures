def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("__", "__", "__")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("__", "__", "__")
    print(board[2][0], "|", board[2][1], "|", board[2][2])

def is_match_over(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
    return True

def vertical_sum(board, status):
    for i in range(0, 3):
        summ = 0
        for j in range(0, 3):
            summ = summ + board[j][i]
        if summ == 33 or summ == 51:
            status = summ
            break
    return status

def horizontal_sum(board, status):
    for i in range(0, 3):
        summ = 0
        for j in range(0, 3):
            summ = summ + board[i][j]
        if summ == 33 or summ == 51:
            status = summ
            break
    return status

def diagonal_sum(board, status):
    if (board[0][0] + board[1][1] + board[2][2] == 33 or board[0][0] + board[1][1] + board[2][2] == 51) or (board[0][2]+board[1][1]+board[2][0] == 33 or board[0][2]+board[1][1]+board[2][0] == 51):
        if board[0][0] + board[1][1] + board[2][2] or board[2][0]+board[1][1]+board[0][2] == 33:
            status = 33
        else:
            status = 51
    return status

def winning_status(board):
    status = 0
    status = vertical_sum(board, status) or horizontal_sum(board, status) or diagonal_sum(board, status)
    if status != 0:
        if status == 33:
            return "player1"
        else:
            return "player2"
    else:
        return False

def play_tic_tac_toe(board):
    ptr = True
    while not is_match_over(board) and not winning_status(board):
        if ptr:
            while ptr:
                p1 = [int(x) for x in input("player1: enter row and coloumn index(0 based):").split()]
                if -1 < p1[0] < 3 and -1 < p1[1] < 3:
                    if board[p1[0]][p1[1]] == 17:
                        print("can not enter in others spot")
                    elif board[p1[0]][p1[1]] == 11:
                        print("already exists ,enter somewhere else")
                    else:
                        board[p1[0]][p1[1]] = 11
                        print_board(board)
                        ptr = not ptr
                else:
                    print("input values should be in range 0 to 2")
        else:
            while not ptr:
                p2 = [int(x) for x in input("player2: enter row and coloumn index(0 based):").split()]
                if -1 < p2[0] < 3 and -1 < p2[1] < 3:
                    if board[p2[0]][p2[1]] == 11:
                        print("can not enter in others spot")
                    elif board[p2[0]][p2[1]] == 17:
                        print("already exists ,enter somewhere else")
                    else:
                        board[p2[0]][p2[1]] = 17
                        print_board(board)
                        ptr = not ptr
                else:
                    print("input values should be in range 0 to 2")

if __name__== '__main__':
    board = [[0 for i in range(3)] for j in range(3)]
    print("Welcome!")
    play_tic_tac_toe(board)
    if winning_status(board):
        print(winning_status(board),"won the game!")
    else:
        print("it's a draw!")




