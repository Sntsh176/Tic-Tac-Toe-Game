

print("Player A will mark First and his mark is 'X' ")
print("Player B will mark Next and his mark is 'O' \n")

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def printmatrix(matrix):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[matrix[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")


def checkhor():
    for i in range(3):
        if (matrix[i][0] == matrix[i][1] == matrix[i][2]) and (matrix[i][0] != 0):
            print("HOR :: The winner is ", matrix[i][0])
            player_win(matrix[i][0])
            return True


def checkver():
    for i in range(3):
        if (matrix[0][i] == matrix[1][i] == matrix[2][i]) and (matrix[0][i] != 0):
            print("VER :: The winner is ", matrix[0][i])
            player_win(matrix[0][i])
            return True


def checkdiag():
    if (matrix[0][0] == matrix[1][1] == matrix[2][2]) and (matrix[0][0] != 0):
        print("DIAG :: the winner is ", matrix[0][0])
        player_win(matrix[0][0])
        return True
    if (matrix[0][2] == matrix[1][1] == matrix[2][0]) and (matrix[0][2] != 0):
        print("DIAG :: the winner is ", matrix[0][2])
        player_win(matrix[0][2])
        return True


def player_win(mark):
    global player_A_win
    global player_B_win
    if mark == 1:
        player_A_win += 1
        print("Wooohh Player A is winner .. !!")
        print("Total win of Player A :", player_A_win)
        print("Total win of Player B :", player_B_win)
    else:
        player_B_win += 1
        print("Wooohh Player B is winner .. !!")
        print("Total win of Player A :", player_A_win)
        print("Total win of Player B :", player_B_win)


def poscheck():
    global posList
    global posEntered
    global cnt
    posList = input("Please enter Location as row,col : ")
    posList = list(posList.strip().split(","))
    if posList in posEntered:
        print('This position is already entered. Please enter another position')
        printmatrix(matrix)
    else:
        posEntered.append(posList)
        print('Positions Entered so far ... ', posEntered)
        cnt += 1


cnt = 0
posEntered = []
posList = ''
player_A_win = 0
player_B_win = 0
play = True

while play:
    while len(posEntered) < 9:
        if cnt % 2 != 1:
            print("Player A : Please enter your Index for 'X' : ")
            poscheck()
            matrix[int(posList[0]) - 1][int(posList[1]) - 1] = 1
        else:
            print("Player B : Please enter your Index for 'O' : ")
            poscheck()
            matrix[int(posList[0]) - 1][int(posList[1]) - 1] = 2

        if checkhor():
            print("The game is over , we have a winner .. !!")
            printmatrix(matrix)
            break
        elif checkver():
            print("The game is over , we have a winner .. !!")
            printmatrix(matrix)
            break
        elif checkdiag():
            print("The game is over , we have a winner .. !!")
            printmatrix(matrix)
            break
    else:
        print("There is no Open Spot and No Winner for this game .. !!")
        print(matrix)
        break

# as after each outer while loop if players want to play then reset the values
    cnt = 0
    posEntered = []
    posList = ''
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    play_val = input("Do you want to play the game again :: for Yes = 'Y' for NO = 'N' : ")
    if play_val.upper() == 'N':
        play = False
        break
