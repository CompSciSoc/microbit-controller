"""
# WARNING!
This is basically pseudocode so completely untested and not to be used elsewhere
"""

import serial
ser = serial.Serial('COM3', 115200)

class MBInput:
    """
    A micro:bit transfers a dictionary of useful data over serial to be used in
    other programs as realtime input i.e. gyro controls. This object recieves
    that data and parses it for easier use.
    """
    
    def get_gyro_data():
        """Returns a tuple of acceleration in x, y, z directions."""
        line = ser.readline().decode('utf-8').strip()
        return (int(line[i]) for i in ["gyro_x", "gyro_y", "gyro_z"])

