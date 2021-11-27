import os
#import time
#data = bytes()
#data = "0"
#data = bytes(data,'utf-8')
# write
dev = os.open("/dev/fpga_led", os.O_RDWR)

#i = 1
#while i <= 255:
#	bytes_val = i.to_bytes(1,'big')
#	os.write(dev, bytes_val)
#	time.sleep(0.1)
#	i*=2


def write_led(index):
	bytes_val = index.to_bytes(1,'big')
	os.write(dev, bytes_val)

write_led(255)
