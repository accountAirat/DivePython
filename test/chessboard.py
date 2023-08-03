import tkinter as tk

BOARDSIDE = 8
COLORS = ('black', 'white')
CELLSIZE = 50


class Chessboard(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N + tk.S + tk.W + tk.E)
        self.makeBoard()

    def makeBoard(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1, minsize=CELLSIZE * BOARDSIDE)
        top.columnconfigure(0, weight=1, minsize=CELLSIZE * BOARDSIDE)

        for i in range(BOARDSIDE):
            for j in range(BOARDSIDE):
                c = (i + j) & 1
                f = tk.Label(self, text=" ", background=COLORS[c])
                f.grid(row=i, column=j, sticky=tk.N + tk.S + tk.W + tk.E)

        for i in range(BOARDSIDE):
            self.rowconfigure(i, weight=1, minsize=CELLSIZE)
            self.columnconfigure(i, weight=1, minsize=CELLSIZE)


board = Chessboard()
board.master.title('Chess board')
board.mainloop()