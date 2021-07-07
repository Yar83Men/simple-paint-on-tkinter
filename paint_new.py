import tkinter as tk
from tkinter import colorchooser, HORIZONTAL

win = tk.Tk()
win.title("Paint on Python")

brush_size = 3
brush_color = "black"

def draw(event):
    global brush_size
    global brush_color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x1, y1, x2, y2,
                       fill=brush_color,
                       outline=brush_color)
def color():
    global brush_color
    brush_color = colorchooser.askcolor()[1]

def size():
    global brush_size
    brush_size = scale.get()

canvas = tk.Canvas(win,
                   width=800,
                   height=600,
                   bg="white")

canvas.grid(row=2, column=0, columnspan=7)
canvas.bind("<B1-Motion>", draw)

button_color = tk.Button(win,
                         text="Цвет",
                         command=color,
                         font=('Arial', 18)
                         )

scale = tk.Scale(win,
                    from_=0,
                    to=50,
                    orient=HORIZONTAL
                    )


button_scale = tk.Button(win,
                         text="Размер",
                         command=size,
                         font=('Arial', 18),
                         )

delete_all_button = tk.Button(text="стереть",
                       bg="silver",
                       fg="black",
                       font=('Tahoma', 14),
                       command=lambda : canvas.delete("all")
                       )


button_color.grid(row=0,column=1)
button_scale.grid(row=0, column=2)
scale.grid(row=0, column=3)
delete_all_button.grid(row=0, column=4)



tk.mainloop()