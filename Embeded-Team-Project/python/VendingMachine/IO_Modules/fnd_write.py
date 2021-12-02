import os

dev = os.open("/dev/fpga_fnd", os.O_RDWR)


def write_fnd(index):
    data = str(index)
    while len(data) < 4:
        data = '0'+data
    data = bytes(data,'utf-8')
    os.write(dev, data)



write_fnd('0000')
