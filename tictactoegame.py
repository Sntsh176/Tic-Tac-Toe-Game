# --------------------Game developed by USAMA EJAZ-----------------------
# -------------------------For Open Use----------------------------

from tkinter import *
import random
from tkinter import messagebox

x = 0
i = 100
nums = []
button = []
check = False
win2 = 2


def menu():
    global win2
    win2 = Tk()
    win2.geometry('318x346')
    win2.title('Tic Tac Toe')
    win2.configure(background='yellow')
    play = Button(win2, text='Play', command=buttons, height=2, width=10, fg='white', bg='red')
    ins = Button(win2, text='Help', command=instructions, height=2, width=10, fg='white', bg='red')
    icon = PhotoImage(file='images/Tic.gif')
    pic = Label(win2, image=icon)
    pic.image = icon
    empty = Label(win2, text='', bg='yellow')
    empty.pack()
    pic.pack()
    empty = Label(win2, text='', bg='yellow')
    empty.pack()
    play.pack()
    ins.pack()


def instructions():
    messagebox.showinfo('Instructions',
                        'It is a single player game. Start by clicking on one of the boxes, an "X" will be positioned at that box and enjoy the game!  (game developed by Usama Ejaz)')


def end():
    global check
    if button[0]['text'] == 'X' and button[1]['text'] == 'X' and button[2]['text'] == 'X':
        check = True
    if button[0]['text'] == 'X' and button[4]['text'] == 'X' and button[8]['text'] == 'X':
        check = True
    if button[0]['text'] == 'X' and button[3]['text'] == 'X' and button[6]['text'] == 'X':
        check = True
    if button[1]['text'] == 'X' and button[4]['text'] == 'X' and button[7]['text'] == 'X':
        check = True
    if button[2]['text'] == 'X' and button[4]['text'] == 'X' and button[6]['text'] == 'X':
        check = True
    if button[3]['text'] == 'X' and button[4]['text'] == 'X' and button[5]['text'] == 'X':
        check = True
    if button[6]['text'] == 'X' and button[7]['text'] == 'X' and button[8]['text'] == 'X':
        check = True
    if button[2]['text'] == 'X' and button[5]['text'] == 'X' and button[8]['text'] == 'X':
        check = True
    check1 = 0
    for k in range(9):
        if button[k]['text'] != '':
            check1 += 1
        if check1 == 10:
            check = True
    if check:
        messagebox.showinfo('Game over', "The end !! (Game developed by Usama Ejaz)")


def buttons():
    global win2
    win2.destroy()
    win = Tk()
    win.geometry('350x348')
    n = 0;
    m = 0

    def B1():
        global i
        if button[1]['text'] != 'X' and button[1]['text'] != 'O':
            button[1]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B2():
        global i
        if button[2]['text'] != 'X' and button[2]['text'] != 'O':
            button[2]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B3():
        global i
        if button[3]['text'] != 'X' and button[3]['text'] != 'O':
            button[3]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B4():
        global i
        if button[4]['text'] != 'X' and button[4]['text'] != 'O':
            button[4]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B5():
        global i
        if button[5]['text'] != 'X' and button[5]['text'] != 'O':
            button[5]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B6():
        global i
        if button[6]['text'] != 'X' and button[6]['text'] != 'O':
            button[6]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B7():
        global i
        if button[7]['text'] != 'X' and button[7]['text'] != 'O':
            button[7]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B8():
        global i
        if button[8]['text'] != 'X' and button[8]['text'] != 'O':
            button[8]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    def B0():
        global i
        if button[0]['text'] != 'X' and button[0]['text'] != 'O':
            button[0]['text'] = 'X'
            end()
            con()
            button[i]['text'] = 'O'

    for i in range(9):
        if m == 3:
            m = 0
            n += 1
        button.append(Button(win, text='', height=3, width=6, fg='red', font="Verdana 19 bold", bg='black'))
        button[i].grid(row=n, column=m)
        m = m + 1
    button[0]['command'] = B0
    button[1]['command'] = B1
    button[2]['command'] = B2
    button[3]['command'] = B3
    button[4]['command'] = B4
    button[5]['command'] = B5
    button[6]['command'] = B6
    button[7]['command'] = B7
    button[8]['command'] = B8


def con():
    global i
    global x
    while True:
        nums.append(i)
        i = random.randint(0, 8)
        if not (i in nums) and button[i]['text'] != 'O' and button[i]['text'] != 'X':
            break


menu()