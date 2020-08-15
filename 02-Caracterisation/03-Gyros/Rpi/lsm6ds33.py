# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
This module provides the LSM6DS33 subclass of LSM6DS for using LSM6DS33 sensors.
"""
from adafruit_lsm6ds import LSM6DS



class LSM6DS33(LSM6DS):  # pylint: disable=too-many-instance-attributes

    """Driver for the LSM6DS33 6-axis accelerometer and gyroscope.

        :param ~busio.I2C i2c_bus: The I2C bus the LSM6DS33 is connected to.
        :param address: The I2C slave address of the sensor

    """

    CHIP_ID = 0x69
    def __init__(self, i2c_bus, address=CHIP_ID):
        super().__init__(i2c_bus, address)
        self._i3c_disable = True