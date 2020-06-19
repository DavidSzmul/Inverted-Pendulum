from tkinter import *

class DialogBox(Toplevel):

    val = []
    def __init__(self, parent, choicelist, text):

        Toplevel.__init__(self, parent)
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2)
        y = (self.winfo_screenheight() // 2)
        self.geometry('+{}+{}'.format(x, y))

        self.parent = parent
        self.label = Label(self, text=text).grid(row=0, column=0, sticky="W")

        self.var = StringVar()
        self.var.set(choicelist[0]) # default option
        self.popupMenu = OptionMenu(self, self.var, *choicelist)
        self.popupMenu.grid(sticky=N+S+E+W, row =1, column = 0)
        self.btn = Button(self, text='OK', command=self.buttonfn).grid(row=2, column=0)
        self.resizable(False, False)
        self.transient(parent)

        self.protocol("WM_DELETE_WINDOW", self._delete_window)

    def _delete_window(self):
        self.var.set('')
        self.destroy()

    def buttonfn(self):
        self.destroy()
    def get_response(self):
        return self.var.get()

if __name__ == '__main__':

    root = Tk('a')
    app = DialogBox(root, ['NSR','NSR (paced)','ST', 'SVT', 'AF', 'VT', 'VF', 'NOISE', 'SAISPAS'],"Select the cardiac event:")
    root.mainloop()
    # wait_window(app)
    print(app.get_response())

