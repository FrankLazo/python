# text = "Texto de pruebas"

# for car in text:
#     print( car )
#     if car == 'x':
#         break
# else:
#     print( "for terminado" )

# class Muestra():
#     propiedad_1 = ""
#     propiedad_2 = ""
#     propiedad_3 = ""
#     prop_4 = "asd"

#     def metodo_1( self ):
#         self.prop_4 = 20

#     def mensaje(self):
#         self.prop_5 = 12356
#         print(self.prop_4)
#         print(self.prop_5)

# muestra = Muestra()
# muestra.mensaje()

from tkinter import *

# Generales --------------------------------------------------------------------

color_main_bg = "#222222"
color_second_bg = "#333333"
color_primary = "#ECBC1C"
color_primary_light = "#E9D698"
color_primary_dark = "#7C6312"

reset_text = "0"

style_general_button = {
    "bg": color_second_bg,
    "fg": color_primary,
    "font": ("Glory", 16),
    "relief": "flat",
    "width": 3,
    "activebackground": color_main_bg,
    "activeforeground": color_primary_light,
    "cursor": "hand2"
}

style_special_button = {
    "bg": color_primary,
    "fg": color_second_bg,
    "font": ("Glory", 16, "bold"),
    "relief": "flat",
    "width": 3,
    "activebackground": color_primary_dark,
    "activeforeground": color_main_bg,
    "cursor": "hand2"
}

grid_style_button = {
    "padx": 2,
    "pady": 2
}

# Raíz -------------------------------------------------------------------------

root = Tk()

root.title("Calculadora")
root.resizable(False, False)
root.iconbitmap("images/python-logo.ico")
root.config(bg=color_main_bg, padx=20, pady=20)

# Frame principal --------------------------------------------------------------

main_frame = Frame()

main_frame.pack()
main_frame.config(bg=color_main_bg)

# Pantalla ---------------------------------------------------------------------

screen_frame = Frame(main_frame, relief="flat")
screen_frame.grid(row=0, column=0, pady=5, sticky="nsew")

# screen_frame.grid_rowconfigure(0, weight=1)
screen_frame.grid_columnconfigure(0, weight=1)

screen_text = Label(screen_frame, text=reset_text, justify="right", bg="red", anchor="e")
screen_text.grid(sticky="nsew")

# Botones ----------------------------------------------------------------------

button_frame = Frame(main_frame)
button_frame.grid(row=1, column=0)
button_frame.config(bg=color_main_bg)

def action():
    pass

button_7 = Button(button_frame, text="7", command=action, **style_general_button)
button_7.grid(row=1, column=0, **grid_style_button)

button_8 = Button(button_frame, text="8", command=action, **style_general_button)
button_8.grid(row=1, column=1, **grid_style_button)

button_9 = Button(button_frame, text="9", command=action, **style_general_button)
button_9.grid(row=1, column=2, **grid_style_button)

button_4 = Button(button_frame, text="4", command=action, **style_general_button)
button_4.grid(row=2, column=0, **grid_style_button)

button_5 = Button(button_frame, text="5", command=action, **style_general_button)
button_5.grid(row=2, column=1, **grid_style_button)

button_6 = Button(button_frame, text="6", command=action, **style_general_button)
button_6.grid(row=2, column=2, **grid_style_button)

button_1 = Button(button_frame, text="1", command=action, **style_general_button)
button_1.grid(row=3, column=0, **grid_style_button)

button_2 = Button(button_frame, text="2", command=action, **style_general_button)
button_2.grid(row=3, column=1, **grid_style_button)

button_3 = Button(button_frame, text="3", command=action, **style_general_button)
button_3.grid(row=3, column=2, **grid_style_button)

button_0 = Button(button_frame, text="0", command=action, **style_general_button)
button_0.grid(row=4, column=0, **grid_style_button)

button_point = Button(button_frame, text=".", command=action, **style_general_button)
button_point.grid(row=4, column=1, **grid_style_button)

button_equal = Button(button_frame, text="=", command=action, **style_general_button)
button_equal.grid(row=4, column=2, **grid_style_button)

# OPERADORES SUPERIOR

button_reset = Button(button_frame, text="C", command=action, **style_general_button)
button_reset.grid(row=0, column=0, **grid_style_button)

button_delete = Button(button_frame, text="Del", command=action, **style_general_button)
button_delete.grid(row=0, column=1, **grid_style_button)

button_percent = Button(button_frame, text="%", command=action, **style_general_button)
button_percent.grid(row=0, column=2, **grid_style_button)

# OPERADORES LATERAL (ARITMETICOS)

button_divide = Button(button_frame, text="/", command=action, **style_general_button)
button_divide.grid(row=0, column=3, **grid_style_button)

button_multiply = Button(button_frame, text="x", command=action, **style_general_button)
button_multiply.grid(row=1, column=3, **grid_style_button)

button_subtract = Button(button_frame, text="-", command=action, **style_general_button)
button_subtract.grid(row=2, column=3, **grid_style_button)

button_add = Button(button_frame, text="+", command=action, **style_special_button)
button_add.grid(row=3, column=3, rowspan=2, sticky="ns", **grid_style_button)



root.mainloop()
