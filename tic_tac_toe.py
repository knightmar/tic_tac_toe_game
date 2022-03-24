import tkinter as tk

tab = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def check_victory():
    #ligne 1
    if tab[0][0] != -1 and tab[0][0] == tab[0][1] and tab[0][0] == tab[0][2]:
        print("you win")
    #ligne 2
    elif tab[1][0] != -1 and tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2]:
        print("you win")
    #ligne 3
    elif tab[2][0] != -1 and tab[2][0] == tab[2][1] and tab[3][0] == tab[2][2]:
        print("you win")
    #colone 1
    if tab[0][0] != -1 and tab[0][0] == tab[1][0] and tab[0][0] == tab[2][0]:
        print("you win")
    #colone 2
    if tab[0][1] != -1 and tab[0][1] == tab[1][1] and tab[0][1] == tab[2][1]:
        print("you win")
    #colone 3
    if tab[0][2] != -1 and tab[0][2] == tab[1][2] and tab[0][2] == tab[2][2]:
        print("you win")



def debug_clear():
    app.field.create_rectangle(0, 0, 500, 500, fill="white")
    drawGame()


def drawGame():
    app.field.create_line(500 / 3, 0, 500 / 3, 600)
    app.field.create_line((500 / 3) * 2, 0, (500 / 3) * 2, 600)
    app.field.create_line(0, 500 / 3, 600, 500 / 3)
    app.field.create_line(0, (500 / 3) * 2, 600, (500 / 3) * 2)


def getClicPos(event):
    line = 0
    column = 0
    mouseX = event.x
    mouseY = event.y
    print(mouseX)
    print(mouseY)
    if 0 < mouseX < 500 / 3:
        column = 1
    elif 500 / 3 < mouseX < (500 / 3) * 2:
        column = 2
    elif (500 / 3) * 2 < mouseX < 500:
        column = 3
    if 0 < mouseY < 500 / 3:
        line = 1
    elif 500 / 3 < mouseY < (500 / 3) * 2:
        line = 2
    elif (500 / 3) * 2 < mouseY < 500:
        line = 3
    print("ligne = " + str(line))
    print("column = " + str(column))
    drawCircles(line, column)


def drawCircles(line, column):
    x1 = 0
    y1 = 0
    if line == 1:
        y1 = 10
    elif line == 2:
        y1 = 500 / 3 + 10
    elif line == 3:
        y1 = (500 / 3) * 2 + 10
    if column == 1:
        x1 = 10
    elif column == 2:
        x1 = 500 / 3 + 10
    elif column == 3:
        x1 = (500 / 3) * 2 + 10

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
