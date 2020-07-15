# import GPIO
# Import SPI

from Encoder import Encoder

class Control:

    angle_l = 0
    angle_r = 0
    command = 0
    PWM = 0
    encoder_left = []
    encoder_right = []

    def __init__(self, encoder_left: Encoder, encoder_right: Encoder):
        self.encoder_left = encoder_left
        self.encoder_right = encoder_right

    def update(self):

        ### Read Encoders
        angle_l = self.encoder_left.get_angle()
        angle_r = self.encoder_left.get_angle()

        ### Read Gyro in I2C

        ### Estimate State (Kalman)

        ### Determine command from PID / LQG ...
        ref = 0
        self.command = (ref-angle_l)*1
        return self.command