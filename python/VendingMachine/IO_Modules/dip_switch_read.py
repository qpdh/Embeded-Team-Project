import os
import time

# 쓰기
dev = os.open("/dev/fpga_dip_switch", os.O_RDWR)

def read_dip_switch():
    data = os.pread(dev,1,0)
    return int.from_bytes(data,'big')
