import math
import RPi.GPIO as GPIO

def read(pin):
    return GPIO.input(pin)

class Encoder:

    pinA_last = 0
    counter = 0
    angle = 0
    resolution = []

    def __init__(self, channnel_A, channel_B, resolution=2048):
        self.resolution = resolution
        self.A = channnel_A
        self.B = channel_B

        ### Init Mode GPIO
        GPIO.setup(self.A, GPIO.IN)
        GPIO.setup(self.B, GPIO.IN)

    def update(self):
        pinA = read(self.A)

        if pinA != self.pinA_last:
            if read(self.B) != self.pinA_last:
                self.counter += 1

            else:
                self.counter -= 1
        else:
            self.pinA_last = pinA

        self.angle = 2*math.pi * self.counter / self.resolution
        return self.angle

    def get_angle(self):
        return self.angle