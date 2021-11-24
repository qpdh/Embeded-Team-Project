import os
import time
data = bytes()
#data = ['h', 'e', 'l', 'l']
#data = "hello World"
# 쓰기
dev = os.open("/dev/fpga_dip_switch", os.O_RDWR)
#os.write(dev, data)
#os.lseek(dev, 0, os.SEEK_SET)
# 읽기
while True:
	data = os.pread(dev,1,0)
	print("data",data)
	time.sleep(1)
