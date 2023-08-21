import tkinter as tk

BRD_ROWS = BRD_COLS = 8
CELL_SZ = 100

root = tk.Tk()

canvas = tk.Canvas(root, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

cell_colors = ['white', 'black']
ci = 0  # color index

for row in range(BRD_ROWS):
    for col in range(BRD_COLS):
        x1, y1 = col * CELL_SZ, row * CELL_SZ
        x2, y2 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ
        canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

        ci = not ci

    ci = not ci

canvas.pack()

root.mainloop()