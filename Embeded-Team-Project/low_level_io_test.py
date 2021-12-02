import os

data = bytes()
data = ['h', 'e', 'l', 'l']
data = "hello World"
# 쓰기
dev = os.open("/dev/fpga_text_lcd", os.O_RDWR)
os.write(dev, data)
os.lseek(dev, 0, os.SEEK_SET)
# 읽기
data = os.read(dev, 16)
result = data.decode('utf-8')
print(result)
