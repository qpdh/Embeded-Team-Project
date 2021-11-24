import os

data = bytes()
data = ['h', 'e', 'l', 'l']
data = "LHJ             LHJ aa"
data = bytes(data,'utf-8')
# write
dev = os.open("/dev/fpga_text_lcd", os.O_RDWR)
os.write(dev, data)

