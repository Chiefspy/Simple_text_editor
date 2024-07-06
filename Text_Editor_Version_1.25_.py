from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def copy(text):
    copied_text = text.get(1.0, END)

    return copied_text


def delete(text):
    if messagebox.askyesno(title="askyesno",
                           message="Are you sure you want to delete all text inside the text area? All unsaved progress will be lost."):
        text.delete(1.0, END)
    else:
        return


def paste(copied_text, text):
    text.insert(INSERT, copied_text)


def saveFile(types, text):
    file = filedialog.asksaveasfile(title="ask save as file",
                                    initialdir=r"\home",
                                    filetypes=types)
    if file is None:
        return
    file.write(text.get(1.0, END))
    file.close()


def openFile(types, text):
    try:
        filepath = str(filedialog.askopenfilename(title="ask open file name",
                                                  initialdir=r"/home",
                                                  filetypes=types))
        with open(filepath, 'r') as f:
            text.insert(INSERT, f.read())
    except FileNotFoundError as e:
        messagebox.showerror(title="show error", message=f"{e}")


def closeFile(window):
    if messagebox.askyesno(title="ask yes no",
                           message="Are you sure you want to exit? All unsaved progress will be lost."):
        window.destroy()
    else:
        return

def create_window(window):
    new_window = Toplevel(window)
    # Feature not complete 

def main():
    window = Tk()

    window.title("Simple Text Editor")

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

    fileMenu.add_command(label="save", command=lambda: saveFile(filetypes, text), image=saveImage, compound=LEFT)
    fileMenu.add_command(label="Open", command=lambda: openFile(filetypes, text), image=openImage, compound=LEFT)

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=lambda: closeFile(window), image=exitImage, compound=LEFT)

    editMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=editMenu, label="edit")

    editMenu.add_command(label="Copy", command=lambda: copy(text), compound=LEFT, image=copyImage)
    editMenu.add_command(label="Paste", command=lambda: paste(copy(), text), compound=LEFT, image=pasteImage)

    editMenu.add_separator()

    editMenu.add_command(label="delete", command=lambda: delete(text), compound=LEFT, image=deleteImage)

    optionsMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=optionsMenu, label="options")

    optionsMenu.add_command(label="Create new window", command=lambda: create_window(window))

    text = Text(window, padx=20, pady=20, font=("Ink free", 20), width=40, height=20)
    text.pack()


    window.mainloop()

if __name__ == '__main__':
    main()

