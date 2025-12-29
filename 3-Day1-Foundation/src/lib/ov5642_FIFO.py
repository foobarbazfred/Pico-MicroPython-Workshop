#
#  ov5642_FIFO.py
#
from machine import Pin

FIFO_REGS=(0x00, 0x01,  0x03, 0x04,  0x06, 0x3c, 0x3d,  0x40, 0x41, 0x42, 0x43, 0x44, )
FIFO_REG_NAMES=('TEST     ','CaptCtrl ','TimReg   ','FIFO Ctrl','GPIO Wr  ','FIFO     ','FIFO     ','FirmV    ','SyncCap  ','FIFO_L   ','FIFO_M   ','FIFO_H   ')

FIFO_REG_WRITE_FLAG = 0x80

ARDUCHIP_FIFO = 0x04

FIFO_CLEAR_MASK = 0x01
FIFO_START_MASK = 0x02
FIFO_RDPTR_RST_MASK = 0x10
FIFO_WRPTR_RST_MASK = 0x20

CAPTURE_DONE_FLAG = 0x08

#
# usage
#
# spi = TFTSetup.hspi
# cs = Pin(15, Pin.OUT)
#
#  fifo = OV5642FIFO(spi, cs)


class OV5642FIFO:

    def __init__(self, spi, cs):
       self.spi = spi   
       self.cs = cs

    def clear_fifo_flag(self):
        self.wr_reg(ARDUCHIP_FIFO, FIFO_CLEAR_MASK);
    
    def flush_fifo(self):
        self.wr_reg(ARDUCHIP_FIFO, FIFO_CLEAR_MASK);
    
    def start_capture(self):
        self.wr_reg(ARDUCHIP_FIFO, FIFO_START_MASK);
    
    def take_picture(self):
        self.flush_fifo()
        self.start_capture()
        # wait until "camera capture done"
        while not (self.rd_reg(0x41) & CAPTURE_DONE_FLAG):
             pass

    def show_sync(self):
        while True:
            flg = self.rd_reg(0x41)
            #print(flg, end="")
            if not (flg & 1):
                print("[sync]", end="")
    
    def dump_img(self):
        for i in range(256):
            val = self.rd_reg(0x3d)          # single FIFO read
            print("{:02x} ".format(val), end="")
            if (i + 1) % 16 == 0:
                print("")
    
    def read_pixels(self, buf):
        self.cs.off()
        self.spi.write(bytes([0x3c]))      # burst FIFO read
        self.spi.readinto(buf, 0xff)
        self.cs.on()
    
    def rd_reg(self, addr):
        self.cs.off()
        self.spi.write(bytes([addr]))
        val = self.spi.read(1, 0xff)[0]
        self.cs.on()
        return val
    
    def wr_reg(self, addr, val):
        self.cs.off()
        self.spi.write(bytes([addr | FIFO_REG_WRITE_FLAG]))
        self.spi.write(bytes([val]))
        self.cs.on()
    
    def show_regs(self):
        for i in range(len(FIFO_REGS)):
            addr = FIFO_REGS[i]
            name = FIFO_REG_NAMES[i]
            print("{:s}(0x{:02x}): ".format(name, addr), end="")
            print("{:02x}".format(self.rd_reg(addr)))
    
