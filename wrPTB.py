from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import serial.tools.list_ports

class wrPTB:

    def portArduino(self):
        lists = sorted(list(serial.tools.list_ports.comports()))
        boards_usb = ['CH340', 'Arduino', 'USB Serial Port', 'FTDI']
        for x in lists:
            for y in boards_usb:
                if x[1].find(y) != -1:
                    return x[0]

    def __init__(self):
        self.board = PyMata3(com_port=self.portArduino())
        self.TRLIGHT_RED = 8
        self.TRLIGHT_YELLOW = 7
        self.TRLIGHT_GREEN = 2
        self.BOARD_LED = 13
        self.ON = 1
        self.OFF = 0

    def blink(self):
        print('Press Ctrl+C to Exit')
        self.board.set_pin_mode(self.BOARD_LED, Constants.OUTPUT)
        while True:
            try:
                print("LED On")
                self.board.digital_write(self.BOARD_LED, self.ON)
                self.board.sleep(1.0)
                print("LED Off")
                self.board.digital_write(self.BOARD_LED, self.OFF)
                self.board.sleep(1.0)
            except (KeyboardInterrupt, SystemExit):
                self.board.digital_write(self.BOARD_LED, self.OFF)
                self.board.shutdown()

    def sleep(self, time):
        self.board.sleep(time)
                
    def traffic(self, R=0, Y=0, G=0):
        self.board.set_pin_mode(self.TRLIGHT_RED, Constants.OUTPUT)
        self.board.set_pin_mode(self.TRLIGHT_YELLOW, Constants.OUTPUT)
        self.board.set_pin_mode(self.TRLIGHT_GREEN, Constants.OUTPUT)
        
        if R == 0:
            self.board.digital_write(self.TRLIGHT_RED, self.OFF)
        else:
            self.board.digital_write(self.TRLIGHT_RED, self.ON)
        
        if Y == 0:
            self.board.digital_write(self.TRLIGHT_YELLOW, self.OFF)
        else:
            self.board.digital_write(self.TRLIGHT_YELLOW, self.ON)
        
        if G == 0:
            self.board.digital_write(self.TRLIGHT_GREEN, self.OFF)
        else:
            self.board.digital_write(self.TRLIGHT_GREEN, self.ON)
            
        
if __name__ == "__main__":
    ptb=wrPTB()
    print('PyTechBrain at port: ', ptb.portArduino())
    ptb.traffic(R=1)
    ptb.sleep(2)
    ptb.traffic(R=1, Y=1)
    ptb.sleep(2)
    ptb.traffic(G=1)
    ptb.sleep(2)
    ptb.traffic(Y=1)
    ptb.sleep(2)
    ptb.traffic()
    ptb.blink()

