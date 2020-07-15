import time
import threading

class FPS_loop:

    # Global Parameters
    RT_FPS = []
    counter = 0

    def __init__(self, fps=4096, display_rt=0):
        self.loop_running = False
        self.FPS = fps
        self.display_RT = display_rt
        self.nb_display = int(fps*display_rt)

    def loop(self):
        i = 0
        t_ideal = time.time()
        p_t_real = t_ideal- 1/self.FPS
        t_real = t_ideal

        # New update of FPS estimation (in s)
        ctr_display = 0
        while self.loop_running:
            t_ideal += 1 / self.FPS

            #### Programm to run at fixed step
            self.inner_loop()

            #### Display
            ctr_display += 1
            if (self.nb_display>0 and ctr_display >= self.nb_display):
                ctr_display = 0
                self.RT_FPS = self.nb_display / (t_real - p_t_real)
                print('FPS: ' + str(self.RT_FPS))
                p_t_real = t_real

            #### End of Programm
            t_real = time.time()
            time.sleep(max(0, t_ideal - t_real))
        return

    def inner_loop(self):
        print('Hello')
        self.counter += 1
        if self.counter >= 10000:
            self.loop_running = False

    def start_loop(self):
        self.loop_running = True
        thread_FPS = threading.Thread(target=self.loop, args=())
        thread_FPS.start()

    def stop_loop(self):
        self.loop_running = False

if __name__ == "__main__":
    Loop = FPS_loop(display_rt=0.5)
    Loop.start_loop()
    # Loop.stop_loop()
    print("End of script")
