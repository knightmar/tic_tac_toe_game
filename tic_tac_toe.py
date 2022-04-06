import random
import tkinter as tk
import tkinter.ttk as ttk

bloc_size = 166.6666666667
total_size = 500
wo_win = -1
player_turn = random.randint(0, 1)
print("player_turn " + str(player_turn))
tab = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def launchGame():
    global tab
    global info_field
    tab = [[-1, -1, -1],
           [-1, -1, -1],
           [-1, -1, -1]]

    if launch_game_btn.winfo_exists():
        launch_game_btn.destroy()
    if result.winfo_exists():
        result.destroy()
    if info_field.winfo_exists():
        info_field.destroy()

    app.main_field = tk.Canvas(app, bg="white", width=600, height=500)
    info_field = tk.Canvas(app, bg="white", width=600, height=200)

    app.main_field.bind("<Button-1>", getClicPos)
    app.main_field.pack()

    info_field.pack()

    # if player_turn == 0:
    #     print(player_turn)
    #     info_field.create_line(20, 20, 150, 150, width=2)
    #     info_field.create_line(20, 150, 150, 20, width=2)
    # if player_turn == 1:
    #     print(player_turn)
    #
    #     info_field.create_oval(20, 20, 150, 150, fill='red')

    drawGame()
    showInfos()


def showInfos():
    # if to_display == 1 or to_display == 0:
    #
    info_field.create_rectangle(10, 10, 170, 170, fill='white')
    info_field.create_line(10, 10, 170, 10)
    info_field.create_line(10, 170, 170, 170)
    info_field.create_line(10, 10, 10, 170)
    info_field.create_line(170, 10, 170, 170)
    if player_turn == 0:
        info_field.create_line(20, 20, 150, 150, width=2)
        info_field.create_line(20, 150, 150, 20, width=2)

    if player_turn == 1:
        info_field.create_oval(20, 20, 150, 150, fill='red')


def getPlayerToPlay():
    global player_turn
    print(player_turn)
    if player_turn == 0:
        player_turn = 1
    elif player_turn == 1:
        player_turn = 0
    return player_turn


def transform(id):
    global wo_win
    name = ""
    if id == -1:
        name = None
    elif id == 0:
        name = "O"
    elif id == 1:
        name = "X"
    wo_win = name
    return name


def show_results():
    global wo_win
    global result
    global launch_game_btn
    app.main_field.create_rectangle(0, 0, 500, 500, fill="white")
    app.main_field.destroy()
    info_field.create_rectangle(0, 0, 500, 500, fill="white")
    info_field.destroy()
    result = ttk.Label(app, text="Bravo " + wo_win + "! Vous avez gagné !", background='white')
    result.pack()
    launch_game_btn = ttk.Button(app, text="Jouer a nouveau", command=launchGame)
    launch_game_btn.pack()


def check_victory():
    # ligne 1
    if tab[0][0] != -1 and tab[0][0] == tab[0][1] and tab[0][0] == tab[0][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()
        # wo_win = transform(tab[0][0])
    # ligne 2
    elif tab[1][0] != -1 and tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2]:
        print("you win ," + transform(tab[1][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # ligne 3
    elif tab[2][0] != -1 and tab[2][0] == tab[2][1] and tab[2][0] == tab[2][2]:
        print("you win ," + transform(tab[2][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 1
    if tab[0][0] != -1 and tab[0][0] == tab[1][0] and tab[0][0] == tab[2][0]:
        print("you win ," + transform(tab[0][0]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 2
    if tab[0][1] != -1 and tab[0][1] == tab[1][1] and tab[0][1] == tab[2][1]:
        print("you win ," + transform(tab[0][1]))
        show_results()

        # wo_win = transform(tab[0][0])
    # colone 3
    if tab[0][2] != -1 and tab[0][2] == tab[1][2] and tab[0][2] == tab[2][2]:
        print("you win ," + transform(tab[0][2]))
        show_results()
    # diagonale gauche
    if tab[0][0] != -1 and tab[0][0] == tab[1][1] and tab[0][0] == tab[2][2]:
        print("you win ," + transform(tab[0][0]))
        show_results()

    if tab[0][2] != -1 and tab[0][2] == tab[1][1] and tab[0][2] == tab[2][0]:
        print("you win ," + transform(tab[0][2]))
        show_results()
        # wo_win = transform(tab[0][0])


def drawGame():
    app.main_field.create_line(500 / 3, 0, 500 / 3, 600, width=2)
    app.main_field.create_line((500 / 3) * 2, 0, (500 / 3) * 2, 600, width=2)
    app.main_field.create_line(0, 500 / 3, 600, 500 / 3, width=2)
    app.main_field.create_line(0, (500 / 3) * 2, 600, (500 / 3) * 2, width=2)
    app.main_field.create_line(0, 501, 500, 501, width=2)


def getClicPos(event):
    # print("win :" + str(wo_win))

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
    showInfos()
    if player == 0:
        tab[line - 1][column - 1] = 0
        drawCircles(line, column)
    elif player == 1:
        tab[line - 1][column - 1] = 1
        drawCross(line, column)
    # print(player_turn)
    #
    # print(mouseX)
    # print(mouseY)
    # print("-" * 7)


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
    app.main_field.create_line(x1, y1, x2, y2, width=5)
    app.main_field.create_line(x2, y1, x1, y2, width=5)

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
    app.main_field.create_oval(x1, y1, x2, y2, fill='red')
    check_victory()


app = tk.Tk()
app.title('tic tac toe')
app.geometry('500x700')
app.config(bg='#FFFFFF')

app.resizable(False, False)

launch_game_btn = ttk.Button(app)
result = ttk.Label(app)

info_field = tk.Canvas(app, bg="white", width=600, height=200)

launchGame()
app.mainloop()
