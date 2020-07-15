import math
# import GPIO

A = 0
B = 0
def read(pin):
    return 0

class Encoder:

    pinA_last = 0
    counter = 0
    angle = 0
    resolution = []

    def __init__(self, resolution=2048):
        self.resolution = resolution

    def update(self):
        pinA = read(A)

        if pinA != self.pinA_last:
            if read(B) != self.pinA_last:
                self.counter += 1

            else:
                self.counter -= 1
        else:
            self.pinA_last = pinA

        # self.angle = 2*math.pi * self.counter / self.resolution
        self.angle+=1
        return self.angle

    def get_angle(self):
        return self.angle