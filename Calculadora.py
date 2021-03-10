from tkinter import *
import parser

root= Tk()
root.title("Moncalculator")

display = Entry(root)
display.grid(row=1, columnspan=6, padx= 5, pady= 5)
# padx y pady, el espacio entre el borde y el display
# sticky=W+E hace que abarque todo el ancho posible de la columna
# columnspan=2 es la cantidad de columnas que abarca, en este caso 2

i=0
# iremos aumenando i de a 1, para que al escribir los nros no se escriban en el mismo espacio, tiene q correr hacia la derecha

def get_numbers(n):
    global i
    display.insert(i,n)
    i+=1

def operation(operator):
    global i
    operator_length= len(operator)
    display.insert(i, operator)
    i+= operator_length

def clear_display():
    display.delete(0,END)

def undo():
    display_state= display.get()
    if len(display_state):
        display_new_state= display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0, "error")

def calculate():
    display_state= display.get()
    try:
        math_expression= parser.expr(display_state).compile()
        result= eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, "error")

# Buttons numeric

Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0, sticky= W+E)
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1, sticky= W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2, sticky= W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column=0, sticky= W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1, sticky= W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2, sticky= W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0, sticky= W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1, sticky= W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2, sticky= W+E)

Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1, sticky= W+E)

# Buttons operations


Button(root, text="+", command=lambda:get_numbers("+")).grid(row=3, column=3, sticky= W+E)
Button(root, text="-", command=lambda:get_numbers("-")).grid(row=4, column=3, sticky= W+E)
Button(root, text="*", command=lambda:get_numbers("*")).grid(row=2, column=4, sticky= W+E)
Button(root, text="=", command=lambda:calculate()).grid(row=5, column=3, sticky=W+E, columnspan=2)

Button(root, text="←", command=lambda:undo()).grid(row=2, column=4, sticky= W+E)
Button(root, text="AC", command=lambda:clear_display()).grid(row=2, column=3, sticky= W+E)
Button(root, text="**", command=lambda:get_numbers("**")).grid(row=3, column=4, sticky= W+E)
Button(root, text="^2", command=lambda:get_numbers("^2")).grid(row=4, column=4, sticky= W+E)
Button(root, text="(", command=lambda:get_numbers("(")).grid(row=5, column=0, sticky= W+E)
Button(root, text=")", command=lambda:get_numbers(")")).grid(row=5, column=2, sticky= W+E)


root.mainloop()
