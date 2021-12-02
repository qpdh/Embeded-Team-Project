import os

dev = os.open("/dev/fpga_step_motor", os.O_RDWR)


def start_step_motor():
    print('step motor start')
    data = b'\x01\x00\xff'
    os.write(dev, data)

def stop_step_motor():
    print('step motor stop')
    data =b'\x00\x00\x00'
    os.write(dev,data)