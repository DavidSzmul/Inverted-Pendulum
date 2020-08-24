# import GPIO
# Import SPI

from Encoder import Encoder
from IMU import IMU
from PID import PID
from Motors import Motors
from Switch import Switch

class Control:

    # Fixed Parameters (for Segway)
    P_stab = 10
    I_stab = 1
    D_stab = 200

    P_position = 1
    I_position = 0.1
    D_position = 20

    Integrator_max = -1
    Integrator_min = 1

    # State of system

    ref_stab = 0   # Set Point of the feedback control (rad)
    ref_position = 0  # Set Point of the feedback control (rad)

    angle_l = 0     # Angle left wheel (rad)
    angle_r = 0     # Angle right wheel (rad)
    angle_imu = []  # Angle of Segway
    command = 0     # command sent to motor right wheel (between [-1,1])

    encoder_left = []
    encoder_right = []
    imu = []
    switch_OnOff = []
    PID_stab = []
    PID_position = []
    Motor_left = []
    Motor_right = []

    def __init__(self, encoder_left: Encoder, encoder_right: Encoder, imu: IMU):

        ### Switch On/Off
        self.switch_OnOff = Switch()

        ### Encoders
        self.encoder_left = encoder_left
        self.encoder_right = encoder_right

        ### IMU
        self.imu = imu

        ### PID
        self.PID_stab = PID(self.P_stab, self.I_stab, self.D_stab)
        self.PID_position = PID(self.P_position, self.I_position, self.D_position)

        ### Motors
        self.Motors = Motors()

    def update(self):

        ### Check activation status of system
        if not self.switch_OnOff.get_status: return

        ### Get desired position
        #### TODO : Add user interface -> For the moment, only a fixed position
        self.ref_position = 0

        ### Read Encoders
        self.angle_l = self.encoder_left.get_angle()
        self.angle_r = self.encoder_left.get_angle()

        ### Read Gyro in I2C
        self.angle_imu = self.imu.get_angle()

        #### TODO : Add Kalman in order to estimate position from Encoders + Accelero + Gyro

        ### Determine command from PID for stabilization and position of segway on x-axis
        command_stab = self.PID_stab(self.ref_stab, self.angle_imu)
        command_position = self.PID_position.update(self.ref_position, (self.angle_l+self.angle_r)/2)
        self.command = min(max(command_stab + command_position,-1),1)

        ### Send command to ESC's and motor
        self.Motors.send(0, self.command)   # LEFT
        self.Motors.send(1, self.command)   # RIGHT