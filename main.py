from tkinter import *

# some window setup
master = Tk()
master.geometry("450x512")
master.title("Tikinter-Takinter-Tokinter")
master.grid_rowconfigure(0, weight=1)
master.grid_rowconfigure(1, weight=1)
master.grid_columnconfigure(0, weight=1)

player = True   # true while it's X's turn, false if it's O's
gameActive = True   # turned false when the game is over

# 2-dimensional list of empty buttons
buttons = [[Button(), Button(), Button()],
           [Button(), Button(), Button()],
           [Button(), Button(), Button()]]

def endGame(winner):
    global gameActive
    gameActive = False
    if winner != "none":
        endText = Label(master, text=winner+" won!", font="Arial, 18")
        endText.grid(row=1, column=0, sticky=N)
    else:
        endText = Label(master, text="Nobody won...", font="Arial, 18")
        endText.grid(row=1, column=0, sticky=N)

def checkBoard(buttons):
    # Check rows
    if buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text']\
            and buttons[0][0]['text'] != "":
        endGame(buttons[0][0]['text'])
    elif buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text']\
            and buttons[1][0]['text'] != "":
        endGame(buttons[1][0]['text'])
    elif buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text']\
            and buttons[2][0]['text'] != "":
        endGame(buttons[2][0]['text'])
    # Check columns
    elif buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text']\
            and buttons[0][0]['text'] != "":
        endGame(buttons[0][0]['text'])
    elif buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text']\
            and buttons[0][1]['text'] != "":
        endGame(buttons[0][1]['text'])
    elif buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text']\
            and buttons[0][2]['text'] != "":
        endGame(buttons[0][2]['text'])
    # Check diagonals
    elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text']\
            and buttons[0][0]['text'] != "":
        endGame(buttons[0][0]['text'])
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text']\
            and buttons[0][2]['text'] != "":
        endGame(buttons[0][2]['text'])
    # Check if the board is full
    isFull = True
    for i in range(len(buttons)):
        for j in range(len(buttons)):
            if buttons[i][j]['text'] == "":
                isFull = False
    if isFull:
        endGame("none")

def buttonPress(i, j):
    global player
    global buttons
    global gameActive
    if player and buttons[i][j]['text'] == "" and gameActive:
        buttons[i][j].config(text="X", fg='red', height=2, width=4, font="Arial, 58")
        player = not player
    elif not player and buttons[i][j]['text'] == "" and gameActive:
        buttons[i][j].config(text="O", fg='blue', height=2, width=4, font="Arial, 58")
        player = not player
    checkBoard(buttons)
    updateTurnText()

def updateTurnText():
    if gameActive:
        if player:
            gameText.config(text="X's turn.")
        else:
            gameText.config(text="O's turn.")

boardFrame = Frame(master, relief=RAISED)
boardFrame.grid(row=0, column=0, sticky=N)

for i in range(len(buttons)):
    for j in range(len(buttons)):
        buttons[i][j] = Button(boardFrame, height=2, width=4, text="", font="Arial, 58")
        buttons[i][j].grid(row=i, column=j, sticky=N+E+W+S)
        buttons[i][j].config(command=lambda ci=i, cj=j: buttonPress(ci, cj))

gameText = Label(master, text="X's turn.", font="Arial, 18")
gameText.grid(row=1, column=0, sticky=N)

while True:
    master.update_idletasks()
    master.update()
