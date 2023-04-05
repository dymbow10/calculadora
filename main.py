from tkinter import *
import calc
import number

opr = ""

def add_to_screen(x): #adds symbol 'x' to the operation queue
    global opr
    opr += str(x)
    result.delete(1.0,'end')
    result.insert(1.0,opr)

def evaluate():
    global opr
    first=number.Number('','')
    second=number.Number('','')
    symbol=""
    for i in range(len(opr)):
        try:
            if opr[i] == '.':
                for j in range(i+1,len(opr)):
                    try:
                        int(opr[j])
                        first.decimal+=opr[j]
                    except:
                        break
            else:
                int(opr[i]) #checks if i is a number
                if i>0:
                    if opr[i-1] != ".":
                        first.integer+=opr[i]
                else:
                    first.integer+=opr[i]
        except:
            symbol+=opr[i] #if i is a symbol, add it to the symbol var
            for j in range(i+1,len(opr)):
                try:
                    if opr[j] == '.':
                        for k in range(j+1,len(opr)):
                            try:
                                int(opr[k])
                                second.decimal+=opr[k]
                            except:
                                break
                    if opr[j-1] != "." and opr[j] != ".":
                        second.integer+=opr[j]
                except:
                    break
            break

    match symbol:
        case "+":
            opr = str(calc.soma(first.getNumber(),second.getNumber()))
        case "-":
            opr = str(calc.sub(first.getNumber(),second.getNumber()))
        case "/":
            opr = str(calc.div(first.getNumber(),second.getNumber()))
        case "*":
            opr = str(calc.multi(first.getNumber(),second.getNumber()))
        case "^":
            opr = str(calc.pow(first.getNumber(),second.getNumber()))
        case "%":
            opr = str(calc.mod(first.getNumber(),second.getNumber()))
        case "!":
            opr = str(calc.fac(first.getNumber()))
        case _:
            opr = "Error"
    result.delete(1.0, "end")
    result.insert(1.0, opr)
    print(first,second)

def clear():
    global opr
    opr = ""
    result.delete(1.0, "end")


window = Tk()
window.geometry("355x400")
window.title("Calculator")
result = Text(window, height=4, width=20, font=("Arial", 24))
result.grid(columnspan=5)

btn_1 = Button(window, text="1", command=lambda:add_to_screen(1), width=5, font=("Arial", 15))
btn_1.grid(row=2, column=0)
btn_2 = Button(window, text="2", command=lambda:add_to_screen(2), width=5, font=("Arial", 15))
btn_2.grid(row=2, column=1)
btn_3 = Button(window, text="3", command=lambda:add_to_screen(3), width=5, font=("Arial", 15))
btn_3.grid(row=2, column=2)
btn_4 = Button(window, text="4", command=lambda:add_to_screen(4), width=5, font=("Arial", 15))
btn_4.grid(row=3, column=0)
btn_5 = Button(window, text="5", command=lambda:add_to_screen(5), width=5, font=("Arial", 15))
btn_5.grid(row=3, column=1)
btn_6 = Button(window, text="6", command=lambda:add_to_screen(6), width=5, font=("Arial", 15))
btn_6.grid(row=3, column=2)
btn_7 = Button(window, text="7", command=lambda:add_to_screen(7), width=5, font=("Arial", 15))
btn_7.grid(row=4, column=0)
btn_8 = Button(window, text="8", command=lambda:add_to_screen(8), width=5, font=("Arial", 15))
btn_8.grid(row=4, column=1)
btn_9 = Button(window, text="9", command=lambda:add_to_screen(9), width=5, font=("Arial", 15))
btn_9.grid(row=4, column=2)
btn_0 = Button(window, text="0", command=lambda:add_to_screen(0), width=5, font=("Arial", 15))
btn_0.grid(row=5, column=1)

btn_plus = Button(window, text="+", command=lambda:add_to_screen("+"), width=5, font=("Arial", 15))
btn_plus.grid(row=2, column=3)
btn_minus = Button(window, text="-", command=lambda:add_to_screen("-"), width=5, font=("Arial", 15))
btn_minus.grid(row=3, column=3)
btn_div = Button(window, text="/", command=lambda:add_to_screen("/"), width=5, font=("Arial", 15))
btn_div.grid(row=4, column=3)
btn_mul = Button(window, text="*", command=lambda:add_to_screen("*"), width=5, font=("Arial", 15))
btn_mul.grid(row=5, column=3)
btn_pow = Button(window, text="^", command=lambda:add_to_screen("^"), width=5, font=("Arial", 15))
btn_pow.grid(row=2, column=4)
btn_mod = Button(window, text="%", command=lambda:add_to_screen("%"), width=5, font=("Arial", 15))
btn_mod.grid(row=3, column=4)
btn_fac = Button(window, text="!", command=lambda:add_to_screen("!"), width=5, font=("Arial", 15))
btn_fac.grid(row=4, column=4)
btn_dot = Button(window, text=".", command=lambda:add_to_screen("."), width=5, font=("Arial", 15))
btn_dot.grid(row=5, column=4)

btn_eq = Button(window, text="=", command=evaluate, width=5, font=("Arial", 15))
btn_eq.grid(row=5, column=2)
btn_cls = Button(window, text="C", command=clear, width=5, font=("Arial", 15))
btn_cls.grid(row=5, column=0)

window.mainloop()