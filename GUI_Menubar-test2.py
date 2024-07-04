from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def copy():
    copied_text = text.get(1.0, END)

    return copied_text


def delete():
    if messagebox.askyesno(title="askyesno",
                           message="Are you sure you want to delete all text inside the text area? All unsaved progress will be lost"):
        text.delete(1.0, END)
    else:
        return


def paste(copied_text):
    text.insert(INSERT, copied_text)


def saveFile(types):
    file = filedialog.asksaveasfile(title="ask save as file",
                                    initialdir=r"\home",
                                    filetypes=types)
    if file is None:
        return
    file.write(text.get(1.0, END))
    file.close()


def openFile(types):
    try:
        filepath = str(filedialog.askopenfilename(title="ask open file name",
                                                  initialdir=r"/home",
                                                  filetypes=types))
        with open(filepath, 'r') as f:
            text.insert(INSERT, f.read())
    except FileNotFoundError as e:
        messagebox.showerror(title="show error", message=f"{e}")


def closeFile():
    if messagebox.askyesno(title="ask yes no",
                           message="Are you sure you want to exit? All unsaved progress will be lost."):
        window.destroy()
    else:
        return


window = Tk()

window.title("Cool Text Editor")

filetypes = [("All files", "*.*"),
             ("Python file", "*.py"),
             ("Text file", "*.txt"),
             ("HTML file", "*.html"),
             ("Javascript file", "*.js"),
             ("C file", "*.c")]


saveImage = PhotoImage(file="FlopyDisk.png")
openImage = PhotoImage(file="Folder.png")
exitImage = PhotoImage(file="Stop.png")


deleteImage = PhotoImage(file="Delete.png")
copyImage = PhotoImage(file="Copy.png")
pasteImage = PhotoImage(file="paste.png")

menuBar = Menu(window, )
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(menu=fileMenu, label="file")

fileMenu.add_command(label="save", command=lambda: saveFile(filetypes), image=saveImage, compound=LEFT)
fileMenu.add_command(label="Open", command=lambda: openFile(filetypes), image=openImage, compound=LEFT)

fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=closeFile, image=exitImage, compound=LEFT)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(menu=editMenu, label="edit")

editMenu.add_command(label="Copy", command=copy, compound=LEFT, image=copyImage)
editMenu.add_command(label="Paste", command=lambda: paste(copy()), compound=LEFT, image=pasteImage)

editMenu.add_separator()

editMenu.add_command(label="delete", command=delete, compound=LEFT, image=deleteImage)


text = Text(window, padx=20, pady=20, font=("Ink free", 20), width=40, height=20)
text.pack()


window.mainloop()
