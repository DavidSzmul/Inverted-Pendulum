from FPS_loop import FPS_loop
from Encoder import Encoder


class loop_Encoder(FPS_loop):
    encoder_left = []
    encoder_right = []
    angle_left, angle_right = 0, 0

    def __init__(self, channel_l_A=17, channel_l_B=27, channel_r_A=23, channel_r_B=24, resolution=2048, **kwargs):
        super(loop_Encoder, self).__init__(**kwargs)
        self.encoder_left  = Encoder(channel_l_A, channel_l_B, resolution=resolution)
        self.encoder_right = Encoder(channel_r_A, channel_r_B, resolution=resolution)

    def start_loop(self):
        print('Initialization')
        FPS_loop.start_loop(self)

    def inner_loop(self):
        self.angle_left = self.encoder_left.update()
        self.angle_right = self.encoder_right.update()


# main for function call.
if __name__ == "__main__":
    loop_encoder = loop_Encoder(fps=6000, display_rt=0)
    loop_encoder.start_loop()
    print("End of script")
