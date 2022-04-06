import tkinter as tk

window = tk.Tk()
window.geometry('300x300')

# schijf hier tussen je code
x = True


def Lightswitch():
    global x
    if x:
        print('Light on')
        x = False
        button.configure(text="Switch light off =)")
        window.configure(bg="yellow")
    else:
        print('Light off')
        x = True
        button.configure(text="Switch light on =)")
        window.configure(bg="black")


button = tk.Button(text='Switch light on =)', bg='white', fg='black', command=Lightswitch)

button.pack()
# schijf hier tussen je code


window.mainloop()
