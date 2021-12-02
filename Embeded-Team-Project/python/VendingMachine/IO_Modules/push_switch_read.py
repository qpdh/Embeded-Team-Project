import os
import time
data = bytes()

dev = os.open("/dev/fpga_push_switch", os.O_RDWR)

def read_push_switch():
    data = os.pread(dev,9,0)
    return data
