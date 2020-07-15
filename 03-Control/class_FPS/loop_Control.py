from FPS_loop import FPS_loop
from Control import Control
from loop_Encoder import loop_Encoder


class loop_Control(FPS_loop):
    controller = []
    loop_Encoder = []
    command = 0

    def __init__(self, **kwargs):
        super(loop_Control, self).__init__(**kwargs)

        ### Activate encoders
        self.loop_encoder = loop_Encoder(fps=6000, display_rt=0, resolution=2048)
        self.loop_encoder.start_loop()

        ### Link Controller with encoders
        self.controller = Control(encoder_left=self.loop_encoder.encoder_left,
                                  encoder_right=self.loop_encoder.encoder_right)

    def start_loop(self):
        print('Initialization')
        FPS_loop.start_loop(self)

    def inner_loop(self):
        self.command = self.controller.update()
        print(self.command)
        self.counter += 1

        ### Condition to stop loop
        if self.counter >= 200:
            self.loop_running = False
            self.loop_encoder.stop_loop()


# main for function call.
if __name__ == "__main__":
    loop_controller = loop_Control(fps=20, display_rt=1)
    loop_controller.start_loop()
    print("End of script")
