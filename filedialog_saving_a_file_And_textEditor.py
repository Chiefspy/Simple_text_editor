from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def save():
    file = filedialog.asksaveasfile(title="ask save as file",# defaultextension=".txt",
                                    initialdir=r"/home",
                                    filetypes=[
                                        ("Text file", "*.txt"),
                                        ("Python file","*.py"),
                                        ("All files", "*.*"),
                                        ("Bash file", "*.sh"),
                                        ("HTML file", "*.html"),
                                        ("CSS file", "*.css"),
                                        ("Javascript file", "*.js"),
                                        ("Lua file", "*.lua"),
                                        ("PHP file", "*.php")


                                    ])
    if file is None:
        return
    file.write(text.get(1.0, END))
    file.close()


def openFile():
    try:
        file_path =str(filedialog.askopenfilename(title="ask open file name" ,initialdir=r"/home",filetypes=[
                                        ("Text file", "*.txt"),
                                        ("Python file","*.py"),
                                        ("All files", "*.*"),
                                        ("Bash file", "*.sh"),
                                        ("HTML file", "*.html"),
                                        ("CSS file", "*.css"),
                                        ("Javascript file", "*.js"),
                                        ("Lua file", "*.lua"),
                                        ("PHP file", "*.php")
                                    ]))
        file = open(file_path, "r")
        messagebox.showinfo(title="show info", message=file.read())
        file.close()
    except FileNotFoundError as e:
        messagebox.showerror(title="show error", message=e)


def close_window():
    answer = messagebox.askyesno(title="ask yes or no", message="Are you sure you want to close the window? All unsaved progress will be lost")
    if answer:
        window.destroy()
    else:
        return


def display():
    filename = str(filedialog.askopenfilename(title="ask open file name", initialdir="r/home",filetypes=[
        ("All files", "*.*"),
        ("Python file", "*.py"),
        ("Bash file", "*.sh"),
        ("HTML file", "*.html"),
        ("CSS file", "*.css"),
        ("Javascript file", "*.js"),
        ("Lua file", "*.lua"),
        ("Text file", "*.txt")


    ]))
    with open(filename , 'r') as f:
        text.insert(INSERT, f.read())
        

window = Tk()
window.title("Create and open a file")

button = Button(window, text="save", command=save)
button.pack()
button_open = Button(window, text="open", command=openFile)
button_open.pack()
button_close = Button(window, text="close window", command=close_window)
button_close.pack()
buttonDisplay = Button(window, text="display file contents", command=display)
buttonDisplay.pack()
text = Text(window, font=("Ink free", 20),padx=20, pady=20, bg="light yellow")
text.pack()

window.mainloop()
