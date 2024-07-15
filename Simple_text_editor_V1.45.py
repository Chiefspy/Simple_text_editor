from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os


def copy(text):
    copied_text = text.get(1.0, END)

    return copied_text


def delete(text):
    if messagebox.askyesno(title="askyesno",
                           message="Are you sure you want to delete all text inside the text area? All unsaved progress will be lost"):
        text.delete(1.0, END)
    else:
        return


def paste(copied_text, text):
    text.insert(INSERT, copied_text)


def saveFile(types, text, home_dir):
    file = filedialog.asksaveasfile(title="ask save as file",
                                    initialdir=rf"{home_dir}",
                                    filetypes=types)
    if file is None:
        return
    file.write(text.get(1.0, END))
    file.close()


def openFile(types, text, home_dir):
    try:
        filepath = str(filedialog.askopenfilename(title="ask open file name",
                                                  initialdir=rf"{home_dir}",
                                                  filetypes=types))
        with open(filepath, 'r') as f:
            text.insert(INSERT, f.read())
    except FileNotFoundError as e:
        messagebox.showerror(title="show error", message=f"{e}")
    except UnicodeDecodeError as j:
        messagebox.showerror(title="show error", message=f"{j}")


def closeFile(window, event=None):
    if messagebox.askyesno(title="ask yes no",
                           message="Are you sure you want to exit? All unsaved progress will be lost."):
        window.destroy()
    else:
        return

def create_window(window):
    new_window = Toplevel(window)
    notebook = ttk.Notebook(new_window,)
    tab1 = Frame(notebook,)
    tab2 = Frame(notebook,)
    notebook.add(tab1, text="tab1")
    notebook.add(tab2, text="tab2")
    notebook.pack()
    
    label1 = Label(tab1, text="Hello", bg="red", width=50, height=25)
    label1.pack()
    label1.bind("<Button-1>", kys)
    label1.bind("<B1-Motion>", help)

    
    label2 = Label(tab2, text="Goodbye", bg="blue", width=50, height=25)
    label2.pack()
    label2.bind("<Button-1>", kys)
    label2.bind("<B1-Motion>", help)
    new_window.bind("<w>", lambda event: move_up(event, label2))
    new_window.bind("<a>", move_left)
    new_window.bind("<s>", move_down)
    new_window.bind("<d>", move_right)
    new_window.bind("<Up>", move_up)
    new_window.bind("<Down>", move_down)
    new_window.bind("<Left>", move_left)
    new_window.bind("<Right>", move_right)
    
    #Feature not complete 
def move_up(event, widget):
    widget.place(x=widget.winfo_x() , y=widget.winfo_y() - 10)

def move_down(event):
    widget = event.widget
    widget.place(x=widget.winfo_x() , y=widget.winfo_y() + 10)

def move_left(event):
    widget = event.widget
    widget.place(x=widget.winfo_x() - 10 , y=widget.winfo_y())
    
def move_right(event):
    widget = event.widget
    widget.place(x=widget.winfo_x() + 10 , y=widget.winfo_y())

def kys(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def help(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)
    
def main():
    window = Tk()

    window.title("Simple Text Editor")

    home_dir = os.path.expanduser('~')

    window.bind("<Button-3>", lambda event: closeFile(window))


    filetypes = [("All files", "*.*"),
             ("Python file", "*.py"),
             ("Text file", "*.txt"),
             ("HTML file", "*.html"),
             ("Javascript file", "*.js"),
             ("C file", "*.c"),
                 ("CSS file", "*.css")]



    saveImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/FlopyDisk.png")
    openImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Folder.png")
    exitImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Stop.png")

    deleteImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Delete.png")
    copyImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Copy.png")
    pasteImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/paste.png")

    create_WindowImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/new_tab_icon.png")


    menuBar = Menu(window, )
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=fileMenu, label="file")

    fileMenu.add_command(label="save", command=lambda: saveFile(filetypes, text, home_dir), image=saveImage, compound=LEFT)
    fileMenu.add_command(label="Open", command=lambda: openFile(filetypes, text, home_dir), image=openImage, compound=LEFT)

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=lambda: closeFile(window), image=exitImage, compound=LEFT)

    editMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=editMenu, label="edit")

    editMenu.add_command(label="Copy", command=lambda: copy(text), compound=LEFT, image=copyImage)
    editMenu.add_command(label="Paste", command=lambda: paste(copy(text), text), compound=LEFT, image=pasteImage)

    editMenu.add_separator()

    editMenu.add_command(label="delete", command=lambda: delete(text), compound=LEFT, image=deleteImage)

    optionsMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=optionsMenu, label="options")

    optionsMenu.add_command(label="Create new window", command=lambda: create_window(window), compound=LEFT, image=create_WindowImage)

    text = Text(window, padx=20, pady=20, font=("Ink free", 20), width=40, height=20)
    text.pack(expand=True, fill="both")


    window.mainloop()

if __name__ == '__main__':
    main()





