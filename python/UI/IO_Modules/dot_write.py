import os

dev = os.open("/dev/fpga_dot", os.O_RDWR)

#i = 1
#while i <= 255:
#	bytes_val = i.to_bytes(1,'big')
#	os.write(dev, bytes_val)
#	time.sleep(0.1)
#	i*=2


def write_dot(index):
    data = str(index)
    data = bytes(data,'utf-8')
    os.write(dev, data)

