# !/use/bin/env python3
# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

# Part One ***********************************************************

def drawHorizontal(_num):
    return _num * " ---"
def drawVertical(_num):
    return _num * "|   " + "|"
def drawBoard(_num):
    return _num * (drawHorizontal(_num) + "\n" + drawVertical(_num) + "\n") + drawHorizontal(_num)
print(drawBoard(int(input("Enter board size: "))))