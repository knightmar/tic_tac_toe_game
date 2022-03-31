import tkinter as tk

bloc_size = 166.6666666667
total_size = 500

wo_win = -1
player_turn = 0
tab = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def getPlayerToPlay():
    global player_turn
    if player_turn == 0:
        player_turn = 1
    elif player_turn == 1:
        player_turn = 0
    return player_turn


def transform(id):
    name = ""
    if id == -1:
        name = None
    elif id == 0:
        name = "O"
    elif id == 1:
        name = "X"
    return name


def show_results():
    app.field.create_rectangle(0, 0, 500, 500, fill="white")
    app.field.create_text(133, 133, text="Bravo " + transform(tab[0][0]) + "! Vous avez gagné !" )


def check_victory():
    # ligne 1
    if tab[0][0] != -1 and tab[0][0] == tab[0][1] and tab[0][0] == tab[0][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()
        # wo_win = transform(tab[0][0])
    # ligne 2
    elif tab[1][0] != -1 and tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # ligne 3
    elif tab[2][0] != -1 and tab[2][0] == tab[2][1] and tab[2][0] == tab[2][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 1
    if tab[0][0] != -1 and tab[0][0] == tab[1][0] and tab[0][0] == tab[2][0]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 2
    if tab[0][1] != -1 and tab[0][1] == tab[1][1] and tab[0][1] == tab[2][1]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 3
    if tab[0][2] != -1 and tab[0][2] == tab[1][2] and tab[0][2] == tab[2][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])


def debug_clear():
    app.field.create_rectangle(0, 0, 500, 500, fill="white")
    for i in range(3):
        for y in range(3):
            tab[i][y] = -1
    print(tab)
    drawGame()


def drawGame():
    app.field.create_line(500 / 3, 0, 500 / 3, 600)
    app.field.create_line((500 / 3) * 2, 0, (500 / 3) * 2, 600)
    app.field.create_line(0, 500 / 3, 600, 500 / 3)
    app.field.create_line(0, (500 / 3) * 2, 600, (500 / 3) * 2)


def getClicPos(event):
    print("win :" + str(wo_win))

    mouseX = event.x
    mouseY = event.y
    if mouseY == 0:
        mouseY = 1
    line = 0
    column = 0

    if 0 < mouseX < bloc_size:
        column = 1
    elif bloc_size < mouseX < bloc_size * 2:
        column = 2
    elif bloc_size * 2 < mouseX < total_size:
        column = 3
    if 0 < mouseY < bloc_size:
        line = 1
    elif bloc_size < mouseY < bloc_size * 2:
        line = 2
    elif bloc_size * 2 < mouseY < total_size:
        line = 3

    player = getPlayerToPlay()
    if player == 0:
        tab[line - 1][column - 1] = 0
        drawCircles(line, column)
    elif player == 1:
        tab[line - 1][column - 1] = 1
        drawCross(line, column)
    print(player_turn)

    print(mouseX)
    print(mouseY)
    print("-" * 7)


def drawCross(line, column):
    x1 = 0
    y1 = 0
    if line == 1:
        y1 = 10
    elif line == 2:
        y1 = bloc_size + 10
    elif line == 3:
        y1 = bloc_size * 2 + 10
    if column == 1:
        x1 = 10
    elif column == 2:
        x1 = bloc_size + 10
    elif column == 3:
        x1 = bloc_size * 2 + 10

    x2 = x1 + 146.6
    y2 = y1 + 146.6
    app.field.create_line(x1, y1, x2, y2, width=5)
    app.field.create_line(x2, y1, x1, y2, width=5)

    check_victory()


def drawCircles(line, column):
    x1 = 0
    y1 = 0
    if line == 1:
        y1 = 10
    elif line == 2:
        y1 = bloc_size + 10
    elif line == 3:
        y1 = bloc_size * 2 + 10
    if column == 1:
        x1 = 10
    elif column == 2:
        x1 = bloc_size + 10
    elif column == 3:
        x1 = bloc_size * 2 + 10

    x2 = x1 + 146.6
    y2 = y1 + 146.6
    app.field.create_oval(x1, y1, x2, y2, fill='red')
    check_victory()


app = tk.Tk()
debug = tk.Tk()
debug.geometry('100x40')

debug.title("debug")
app.title('tic tac toe')
app.geometry('500x500')
app.config(bg='#FFFFFF')

app.resizable(False, False)

app.field = tk.Canvas(app, bg="white", width=600, height=500)
app.field.bind("<Button-1>", getClicPos)
app.field.pack()

tk.Button(debug, text="clear", command=debug_clear).pack()

drawGame()

app.mainloop()
