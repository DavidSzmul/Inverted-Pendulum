from tkinter import *

class DialogBox:

    val = []
    def __init__(self, parent, choicelist, text):

        self.parent = parent
        self.label = Label(parent, text=text).grid(row=0, column=0, sticky="W")

        self.var = StringVar()
        self.var.set(choicelist[0]) # default option
        self.popupMenu = OptionMenu(parent, self.var, *choicelist)
        self.popupMenu.grid(sticky=N+S+E+W, row =1, column = 0)
        self.btn = Button(parent, text='OK', command=self.buttonfn).grid(row=2, column=0)

    def buttonfn(self):
        self.parent.destroy()
    def get_response(self):
        return self.var.get()

if __name__ == '__main__':

    root = Tk('a')

    frame = Frame(root)
    # root.title("Test")
    new_wind = Toplevel(root)
    # new_wind.transient(root)
    # new_wind.resizable(False, False)
    # new_wind.title("ChoiceBox")
    app = DialogBox(new_wind, ['NSR','NSR (paced)','ST', 'SVT', 'AF', 'VT', 'VF', 'NOISE', 'SAISPAS'],"Select the cardiac event:")
    print(app.get_response())

    root.mainloop()