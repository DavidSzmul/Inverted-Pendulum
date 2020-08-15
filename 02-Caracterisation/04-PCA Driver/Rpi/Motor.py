from __future__ import division
import time
import numpy as np

# Import the PCA9685 module.
import Adafruit_PCA9685

class Motor:
    driver = []
    num_motor = []
    f_sample = 400  # Sample frequency of PWM

    ### Obtained from caracterization (check Carac_PCA_ESC.py)
    real_range_deadzone = (2581, 2653)
    real_range_minmax = (1565, 3910)
    half_range_no_deadzone = 1000

    ### Deduced range of driver
    center_driver = (real_range_deadzone[0] + real_range_deadzone[1]) // 2
    deadzone_driver = real_range_deadzone
    range_driver = (real_range_deadzone[0] - half_range_no_deadzone, real_range_deadzone[1] + half_range_no_deadzone)
    half_range_deadzone = (range_driver[1]-center_driver)//2

    def __init__(self, driver_, num_motor_):
        self.driver = driver_
        self.num_motor = num_motor_
        self.driver.set_pwm_freq(self.f_sample)

    def init_pwm(self):
        self.driver.set_pwm(self.num_motor, 0, self.center_driver)
        ### Need to wait some time before setting another pwm


    def set_pwm(self, pwm):
        # normalized PWM ranged in [-1, 1] (0 is the middle of the deadzone)
        # Need to check during control is deadzone needs to be minimized or not (because of overflow issues)
        pwm = min(max(pwm, -1), 1)

        ### With deadzone
        # command_driver = int(self.center_driver + self.half_range_deadzone*pwm)
        ### Without deadzone
        command_driver = int(self.deadzone_driver[int(pwm>=0)] + self.half_range_no_deadzone * pwm)

        self.driver.set_pwm(self.num_motor, 0, command_driver)

if __name__=="__main__":

    # Initialise the PCA9685 using the default address (0x40).
    Motor_Driver = Adafruit_PCA9685.PCA9685(address=0x40)
    LEFT, RIGHT = 0, 1
    Motor_left, Motor_right = Motor(Motor_Driver,LEFT), Motor(Motor_Driver,RIGHT)

    Motor_left.init_pwm(), Motor_right.init_pwm()
    time.sleep(2)

    for pwm in np.linspace(0, 1, 100):
        Motor_left.set_pwm(pwm)
        time.sleep(0.00001)
    for pwm in np.linspace(1, -1, 200):
        Motor_left.set_pwm(pwm)
        time.sleep(0.00001)
    for pwm in np.linspace(-1, 0, 100):
        Motor_left.set_pwm(pwm)
        time.sleep(0.00001)
    Motor_left.set_pwm(0)