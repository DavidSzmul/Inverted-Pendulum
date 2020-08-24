from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(address=0x40)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Measures obtained from caracterisation (Estimation from ESC datasheet doesn't return accuracy results,
# so the range is directly caracterized)
real_range_deadzone = (2581, 2653)
real_range_minmax = (1565, 3910)
dynamic_active = 1000

# A centered configuration using most of the full range is:
center_esc = (real_range_deadzone[0] + real_range_deadzone[1])//2
range_esc = (real_range_deadzone[0]-dynamic_active, real_range_deadzone[1]+dynamic_active)

f_sample  = 400  # Sample frequency of PWM
pwm.set_pwm_freq(f_sample)
val_stop = 2600

def get_range(val_init, step):
    pwm.set_pwm(0, 0, val_stop)
    print('Initializing')
    time.sleep(2)
    val_move = val_init

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
        # Move servo on channel O between extremes.
        pwm.set_pwm(0, 0, val_move)
        print(int(val_move))
        time.sleep(0.5)
        pwm.set_pwm(0, 0, val_stop)
        time.sleep(1)
        val_move += step

def get_deadzone(val_init, step):
    pwm.set_pwm(0, 0, val_stop)
    pwm.set_pwm(1, 0, val_stop)
    print('Initializing')
    time.sleep(2)
    val_move = val_init

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
        # Move servo on channel O between extremes.
        pwm.set_pwm(0, 0, val_move)
        pwm.set_pwm(1, 0, val_move)
        print(int(val_move))
        time.sleep(0.01)
        val_move += step


###################################################################################################
#### Results prove that the range is asymetric with de deadzone, high difference beween two medians
#### Priority to be centered to the deadzone:
#### -> Restriction of the fullrange in order to stay centered
###################################################################################################

### range_deadzone = (2581, 2653)
### range_minmax = (1565, 3910)

# get_range(1567, -1)       # Get minimum range
# get_range(3905, 1)        # Get maximum range
get_deadzone(2582, -1)    # Get minimum deadzone
# get_deadzone(2652, 1)    # Get maximum deadzone