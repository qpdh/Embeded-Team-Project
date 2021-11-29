import os

#data = bytes()
#data = ['h', 'e', 'l', 'l']
#data = "LHJ             LHJ aa"
#data = bytes(data,'utf-8')
# write
dev = os.open("/dev/fpga_text_lcd", os.O_RDWR)


def write_text_lcd(first, second):
    

    if not (len(first) <=16 and len(second) <= 16):
        return
 
    while len(first) <16:
        first+=' '
    while len(second) <16:
        second+=' '

    data = first+second
    print(data)
    data = bytes(data,'utf-8')
    os.write(dev,data)
