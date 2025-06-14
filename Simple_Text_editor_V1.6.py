from tkinter import *
from tkinter import font, colorchooser, filedialog, messagebox, ttk
import os
# import time
from Ball import *
from time import *
import smtplib
import socket


def about():
    messagebox.showinfo(title="About", message="A Simple open source text editor program , still a work in progress. To use the copy, cut , and paste features make sure to highlight some text and then press a button to use the feature.")


def copy(text):
    text.event_generate("<<Copy>>")


def clear(text):
    if messagebox.askyesno(title="askyesno",
                           message="Are you sure you want to delete all text inside the text area? All unsaved "
                                   "progress will be lost"):
        text.delete(1.0, END)
    else:
        return


def cut(text):
    text.event_generate("<<Cut>>")


def paste(text):
    text.event_generate("<<Paste>>")


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


def enter_email_info():
    entry_window = Tk()
    entry_window.title("Send Email")

    email_frame = Frame(entry_window, )

    title_label = Label(email_frame, text="Enter your info")
    title_label.grid(row=0, column=0, columnspan=2)
    sender_label = Label(email_frame, text="Sender's email:")
    sender_label.grid(row=1, column=0)
    sender = Entry(email_frame, )
    sender.grid(row=1, column=1)
    receiver_label = Label(email_frame, text="Receiver's email :")
    receiver_label.grid(row=2, column=0)
    receiver = Entry(email_frame, )
    receiver.grid(row=2, column=1)
    password_label = Label(email_frame, text="Password:")
    password_label.grid(row=3, column=0)
    password = Entry(email_frame, show="*")
    password.grid(row=3, column=1)
    subject_label = Label(email_frame, text="Subject:")
    subject_label.grid(row=4, column=0)
    subject = Entry(email_frame, )
    subject.grid(row=4, column=1)
    body_label = Label(email_frame, text="Message:")
    body_label.grid(row=5, column=0)
    body = Text(email_frame, )
    body.grid(row=5, column=1)
    submitButton = Button(email_frame, text="send mail",
                          command=lambda: gather_email_info(sender, receiver, password, subject, body))
    submitButton.grid(row=6, column=0, columnspan=2)
    email_frame.pack(expand=True, fill="both")


def gather_email_info(sender, receiver, password, subject, body):
    sender = sender.get()
    receiver = receiver.get()
    password = password.get()
    subject = subject.get()
    body = body.get(1.0, END)
    send_mail(sender, receiver, password, subject, body)


def send_mail(sender, receiver, password, subject, body):
    message = f"""From:{sender}
    To: {receiver}
    Subject: {subject}\n
    {body}
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        messagebox.showinfo(title="show info", message="logged in...")
        server.sendmail(sender, receiver, message)
        messagebox.showinfo(title="show info", message="Email sent")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror(title="show error", message="Unable to login")


def create_time_window():
    time_window = Tk()
    time_window.title("Clock")
    time_window.resizable(False, False)

    time_label = Label(time_window, font=("Arial", 50), fg="#00FF00", bg="black")
    time_label.pack()

    day_label = Label(time_window, font=("Ink Free", 25))
    day_label.pack()

    date_label = Label(time_window, font=("Ink Free", 30))
    date_label.pack()
    update(time_window, time_label, day_label, date_label)


def update(time_window, time_label, day_label, date_label):
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_window.after(1000, update, time_window, time_label, day_label, date_label)


def create_window(window):
    HEIGHT = 500
    WIDTH = 700
    xVelocity = 3
    yVelocity = 2
    new_window = Toplevel(window)
    new_window.geometry("1000x1000")
    notebook = ttk.Notebook(new_window, )
    tab1 = Frame(notebook, )
    tab2 = Frame(notebook, )
    notebook.add(tab1, text="tab1")
    notebook.add(tab2, text="tab2")
    notebook.pack(expand=True, fill="both")

    label1 = Label(tab1, text="Hello", bg="red", width=50, height=25, fg="white")
    label1.place(x=0, y=0)
    label1.bind("<Button-1>", kys)
    label1.bind("<B1-Motion>", help)

    canvas = Canvas(tab2, width=WIDTH, height=HEIGHT)
    canvas.pack()
    label2 = Label(tab2, text="Goodbye", bg="blue", width=50, height=25, fg="white")
    label2.place(x=0, y=0)
    label2.bind("<Button-1>", kys)
    label2.bind("<B1-Motion>", help)

    soccer_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
    basket_ball = Ball(canvas, 0, 0, 50, 2, 2, "orange")
    tennis_ball = Ball(canvas, 0, 0, 25, 3, 3, "green")

    while True:
        if not new_window.winfo_exists():
            break
        x_coordinates = label1.winfo_x()
        y_coordinates = label1.winfo_y()
        if x_coordinates >= WIDTH - 50 or x_coordinates < 0:
            xVelocity = -xVelocity
        if y_coordinates >= HEIGHT - 25 or y_coordinates < 0:
            yVelocity = -yVelocity
        label1.place(x=x_coordinates + xVelocity, y=y_coordinates + yVelocity)
        soccer_ball.move()
        basket_ball.move()
        tennis_ball.move()
        new_window.update()
        # time.sleep(0.01)
        sleep(0.01)



"""
    new_window.bind("<w>", move_up)
    new_window.bind("<a>", move_left)
    new_window.bind("<s>", move_down)
    new_window.bind("<d>", move_right)
    new_window.bind("<Up>", move_up)
    new_window.bind("<Down>", move_down)
    new_window.bind("<Left>", move_left)
    new_window.bind("<Right>", move_right)
    
    # Feature not complete 
    # Feature does not work as intended
def move_up(event):
    widget = event.widget
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
"""


def kys(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def help(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


# currently not working as intended please be patient
def calculator_window():
    global equation_text
    global equation_label
    calculatorWindow = Tk()

    calculatorWindow.title("Calculator")

    calculatorWindow.geometry("500x500")

    calculatorWindow.resizable(False, False)

    equation_text = ""
    equation_label = StringVar()
    equation_label.set("")

    display = Label(calculatorWindow, textvariable=equation_label, bg="white", font=("consolas", 20), width=24,
                    height=2)
    display.pack()

    frame = Frame(calculatorWindow)
    frame.pack()

    button1 = Button(frame, height=4, width=9, text="1", command=lambda: button_press(1))
    button1.grid(row=0, column=0)
    button2 = Button(frame, height=4, width=9, text="2", command=lambda: button_press(2))
    button2.grid(row=0, column=1)
    button3 = Button(frame, height=4, width=9, text="3", command=lambda: button_press(3))
    button3.grid(row=0, column=2)
    button4 = Button(frame, height=4, width=9, text="4", command=lambda: button_press(4))
    button4.grid(row=1, column=0)
    button5 = Button(frame, height=4, width=9, text="5", command=lambda: button_press(5))
    button5.grid(row=1, column=1)
    button6 = Button(frame, height=4, width=9, text="6", command=lambda: button_press(6))
    button6.grid(row=1, column=2)
    button7 = Button(frame, height=4, width=9, text="7", command=lambda: button_press(7))
    button7.grid(row=2, column=0)
    button8 = Button(frame, height=4, width=9, text="8", command=lambda: button_press(8))
    button8.grid(row=2, column=1)
    button9 = Button(frame, height=4, width=9, text="9", command=lambda: button_press(9))
    button9.grid(row=2, column=2)
    button0 = Button(frame, height=4, width=9, text="0", command=lambda: button_press(0))
    button0.grid(row=3, column=0)
    decimal = Button(frame, height=4, width=9, text=".", command=lambda: button_press("."))
    decimal.grid(row=3, column=1)
    equal = Button(frame, height=4, width=9, text="=", command=lambda: equals())
    equal.grid(row=3, column=2)
    plus = Button(frame, height=4, width=9, text="+", command=lambda: button_press("+"))
    plus.grid(row=0, column=3)
    minus = Button(frame, height=4, width=9, text="-", command=lambda: button_press("-"))
    minus.grid(row=1, column=3)
    multiply = Button(frame, height=4, width=9, text="*", command=lambda: button_press("*"))
    multiply.grid(row=2, column=3)
    divide = Button(frame, height=4, width=9, text="/", command=lambda: button_press("/"))
    divide.grid(row=3, column=3)
    clear = Button(calculatorWindow, height=4, width=12, text="clear", command=clears)
    clear.pack()
    # calculatorWindow.mainloop()


def clears():
    global equation_text
    global equation_label
    equation_text = ""
    equation_label.set("")


def equals():
    global equation_text
    global equation_label
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        print(total) # debug print statement that makes sure the program calculates correctly

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
        print("Syntax Error")   # debug print statement that makes sure the program handles exceptions correctly

    except ZeroDivisionError:
        equation_label.set("ZeroDivisionError")
        equation_text = ""
        print("ZeroDivisionError") # debug print statement that makes sure the program handles exceptions correctly


def button_press(num):
    global equation_text
    global equation_label
    
    equation_text = equation_text + str(num)
    
    equation_label.set(equation_text)

    print(f"button pressed {num}, equation text {equation_text}")  # debug statement

    # equation_label = StringVar()
    # equation_label.set(equation_text)


def new_file(window, text_area):
    window.title("Untitled")
    text_area.delete(1.0, END)


def change_color(text_area):
    color = colorchooser.askcolor(title="Pick a color")
    if color[1]:
        text_area.config(fg=color[1])


def change_font(text, font_name):
    current_font = font.Font(font=text["font"])
    font_size = current_font.actual()["size"]
    text.config(font=(font_name, font_size))


def change_fontSize(text, font_size):
    current_font = font.Font(font=text["font"])
    font_name = current_font.actual()["family"]
    text.config(font=(font_name, int(font_size)))


def main():
    window = Tk()

    window.title("Simple Text Editor")

    window.configure()

    window_width = 500
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    home_dir = os.path.expanduser('~')

    window.bind("<Button-3>", lambda event: closeFile(window))

    filetypes = [("All files", "*.*"),
                 ("Python file", "*.py"),
                 ("Text file", "*.txt"),
                 ("HTML file", "*.html"),
                 ("Javascript file", "*.js"),
                 ("C file", "*.c"),
                 ("CSS file", "*.css"),
                 ("C++ file", "*.cpp")]

    programImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/program_icon.png")

    window.iconphoto(True, programImage)

  

    new_fileImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/new_file.png")
    saveImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/FlopyDisk.png")
    openImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Folder.png")
    exitImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Stop.png")

    deleteImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Delete.png")
    copyImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Copy.png")
    cutImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/cut.png")
    pasteImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/paste.png")

    aboutImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/about.png")
    create_WindowImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/new_tab_icon.png")
    clockImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Clock.png")
    sendMailImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/Envelope-Download-PNG-Image.png")
    calculatorImage = PhotoImage(file=rf"{home_dir}/Simple_text_editor/Images/calculator.png")

    menuBar = Menu(window,bg='blue')
    window.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=fileMenu, label="file")

    fileMenu.add_command(label="New", command=lambda: new_file(window, text), image=new_fileImage, compound=LEFT)
    fileMenu.add_command(label="save", command=lambda: saveFile(filetypes, text, home_dir), image=saveImage,
                         compound=LEFT)
    fileMenu.add_command(label="Open", command=lambda: openFile(filetypes, text, home_dir), image=openImage,
                         compound=LEFT)

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=lambda: closeFile(window), image=exitImage, compound=LEFT)

    editMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=editMenu, label="edit")

    editMenu.add_command(label="Copy", command=lambda: copy(text), compound=LEFT, image=copyImage)
    editMenu.add_command(label="Cut", command=lambda: cut(text), compound=LEFT, image=cutImage)
    editMenu.add_command(label="Paste", command=lambda: paste(text), compound=LEFT, image=pasteImage)

    editMenu.add_separator()

    editMenu.add_command(label="clear", command=lambda: clear(text), compound=LEFT, image=deleteImage)

    optionsMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(menu=optionsMenu, label="options")

    optionsMenu.add_command(label="About", command=about, compound=LEFT, image=aboutImage)

    optionsMenu.add_command(label="Create new window", command=lambda: create_window(window), compound=LEFT,
                            image=create_WindowImage)

    optionsMenu.add_command(label="View the current time", command=create_time_window, compound=LEFT, image=clockImage)

    optionsMenu.add_command(label="Send an email", command=enter_email_info, compound=LEFT, image=sendMailImage)

    optionsMenu.add_command(label="Open calculator", command=calculator_window, compound=LEFT, image=calculatorImage)

    font_name = StringVar(window)
    font_name.set("Arial")

    font_size = StringVar(window)
    font_size.set("25")

    text = Text(window, padx=20, pady=20, font=("Ink free", 20), width=40, height=20)
    text.pack(expand=True, fill="both")

    optionsFrame = Frame(window)
    optionsFrame.pack()

    color_button = Button(optionsFrame, text="color", command=lambda: change_color(text))
    color_button.pack(side=LEFT)

    font_box = OptionMenu(optionsFrame, font_name, *font.families(),
                          command=lambda font_name: change_font(text, font_name))
    font_box.pack(side=LEFT)

    size_box = Spinbox(optionsFrame, from_=1, to=25, textvariable=font_size,
                       command=lambda: change_fontSize(text, font_size.get()))
    size_box.pack(side=LEFT)

    window.mainloop()


if __name__ == '__main__':
    main()
