import os
import time
data = bytes()

dev = os.open("/dev/fpga_push_switch", os.O_RDWR)


# 0.5초마다 읽기
while True:
	data = os.pread(dev,9,0)
	print("data",data)
	time.sleep(0.5)
