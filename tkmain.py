from tkinter import Tk, Label, Button, StringVar, Entry, messagebox
class gui:
    plusstr = ""
    def __init__(self, master):
        self.master = master
        master.title(".txt file writer")
        self.label = Label(master, text="")
        self.label.pack()

        self.entry = Entry(master, textvariable=ent, width=50)
        self.entry.pack()
        
        self.plus_button = Button(master, text="Add text", command=self.plus)
        self.plus_button.pack()

        self.newlinebutton = Button(master, text="new line", command=self.newline)
        self.newlinebutton.pack()

        self.close_button = Button(master, text="Close", command=self.closegay)
        self.close_button.pack()


        self.donotkillcomputer_button = Button(master, text="Clear", command=self.clear)
        self.donotkillcomputer_button.pack()

        self.entryname = Entry(master, textvariable=filename, width=25)
        self.entryname.pack()

        self.writebutton = Button(master, text="save", command=self.writefile)
        self.writebutton.pack()

        self.createConsole()
    def plus(self):
        gui.plusstr = ent.get() + " "
        t6.set(t5.get())
        t5.set(t4.get())
        t4.set(t3.get())
        t3.set(t2.get())
        t2.set(t1.get())
        t1.set(t.get())
        t.set(t.get() + gui.plusstr)
        ent.set("")
    def newline(self):
        t.set(t.get() + "\n")
    def clear(self):
        MsgBox1 = messagebox.askquestion('Clear?', 'Are you sure you want to clear text?', icon='warning')
        if MsgBox1 == 'yes':
            t6.set("")
            t5.set("")
            t4.set("")
            t3.set("")
            t2.set("")
            t1.set("")
            t.set("")
            gui.plusstr = ""
        else:
            pass
    def createConsole(self):
    #    self.label6 = Label(self.master, textvariable=t6, width=50, wraplength=350, justify="left", anchor="w")
    #   self.label6.pack()
    #    self.label5 = Label(self.master, textvariable=t5, width=50, wraplength=350, justify="left", anchor="w")
    #    self.label5.pack()
    #    self.label4 = Label(self.master, textvariable=t4, width=50, wraplength=350, justify="left", anchor="w")
    #    self.label4.pack()
    #    self.label3 = Label(self.master, textvariable=t3, width=50, wraplength=350, justify="left", anchor="w")
    #    self.label3.pack()
    #    self.label2 = Label(self.master, textvariable=t2, width=50, wraplength=350, justify="left", anchor="w")
    #    self.label2.pack()
    #    self.label1 = Label(self.master, textvariable=t1, width=50, wraplength=350, justify="left", anchor="w")
    #    self.label1.pack()
        self.label0 = Label(self.master, textvariable=t, width=50, wraplength=350, justify="left", anchor="w")
        self.label0.pack()
    def closegay(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')
        if MsgBox == 'yes':
            root.destroy()
        else:
            pass
    def writefile(self):
        try:
            f = open(str(filename.get()) +".txt")

            MsgBox = messagebox.askquestion('Already exists', 'File already exists. Write?', icon='warning')
            if MsgBox == 'yes':
                file = open(str(filename.get()) + ".txt", "w")
                file.write(str(t.get()))
                file.close()
                messagebox.showinfo('Info', 'File saved')
            else:
                messagebox.showwarning('Warning', 'File was not saved')
        except IOError:
            file = open(str(filename.get()) + ".txt", "w")
            file.write(str(t.get()))
            file.close()
            messagebox.showinfo('Info', 'File saved')
root = Tk()
t = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
filename = StringVar()
ent = StringVar()
my_gui = gui(root)
root.mainloop()
