import tkinter as tk
import tkinter.font as tkFont
from tkinter import Menu
import time
import threading


class Fixed_FPS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Change FPS")

        # self.state("zoomed")
        self.bind('<Escape>', lambda e: self.quit_verify())
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit_verify())

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit_verify(self):
        self.frames[MainPage].set_status_Loop(False)
        self.quit()


class MainPage(tk.Frame):
    # Widgets
    slide_FPS = []
    edit_FPS = []
    var_FPS = []

    # Global Parameters
    flag_FPS_loop = False
    current_FPS = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_Widgets()
        self.start_FPS_Loop()

    def get_status_Loop(self):
        return self.flag_FPS_loop

    def set_status_Loop(self, new_value):
        self.flag_FPS_loop = new_value

    def update_FPS(self):
        self.current_FPS = float(self.var_FPS.get())

    def init_Widgets(self):

        ### SubFrames
        FrameSliders = tk.Frame(self)
        FrameSliders.pack(side=tk.TOP)
        FrameEdits= tk.Frame(self)
        FrameEdits.pack(side=tk.TOP)
        ### SLIDER
        self.var_FPS = tk.DoubleVar()
        self.slide_FPS = tk.Scale(FrameSliders, variable=self.var_FPS, from_=1, to=100000, orient=tk.HORIZONTAL,
                                   resolution=1,
                                   length=1200, width = 30,
                                   command= lambda val:self.update_FPS(), # Not at change of value but every Loop
                                  )
        self.slide_FPS.pack()
        tk.Label(FrameEdits, text="Real FPS:").pack(side=tk.LEFT)
        self.edit_FPS = tk.Entry(FrameEdits)
        self.edit_FPS.pack(side=tk.LEFT)

        ### Init Values
        FPS_init = 1
        self.var_FPS.set(FPS_init)  # frame per seconds
        self.update_FPS()

    def start_FPS_Loop(self):
        self.flag_FPS_loop = True
        ### Definition of thread
        def loop_FPS(self):
            i = 0
            t_ideal = time.time()
            p_t_real = t_ideal
            t_real = t_ideal+1 #ToDebug

            # New update of FPS estimation (in s)
            dt_cycle_display = 0.3
            nb_display = int(self.current_FPS*dt_cycle_display)
            ctr_display = 0

            while self.flag_FPS_loop:
                t_ideal += 1/self.current_FPS

                #### Programm to run at fixed step
                ctr_display += 1
                if (ctr_display>=nb_display):
                    ctr_display = 0
                    nb_display = int(self.current_FPS * dt_cycle_display)
                    # print('FPS: ' + str(nb_display / (t_real - p_t_real)))
                    self.edit_FPS.delete(0, 10000)
                    self.edit_FPS.insert(0, str(nb_display / (t_real - p_t_real)))
                    p_t_real = t_real

                #### End of Programm
                t_real = time.time()
                time.sleep(max(0,t_ideal-t_real))
            return
        thread_FPS = threading.Thread(target=loop_FPS, args=(self,))
        thread_FPS.start()


    ### Definition callbacks
    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        self.is_press = True

        def thread_until_release(obj):
            # read variable "a" modify by thread 2
            while True:
                val = int(obj.linkedObj.v.get()) + obj.step

                ### Check if atteined limits
                if val < obj.linkedObj.min_t or val > obj.linkedObj.max_t: return

                obj.linkedObj.v.set(str(val))
                obj.linkedObj.update_FPS()
                time.sleep(0.3)
                if not obj.is_press: return  # Flag end

        thread1_exe = threading.Thread(target=thread_until_release, args=(self,))
        thread1_exe.start()


# main for function call.
if __name__ == "__main__":

    app = Fixed_FPS()
    # frame = app.frames[MainPage]
    # frame.init_slider()
    # frame.start_FPS_Loop()
    app.mainloop()
    print("End of script")
