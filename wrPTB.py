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

if __name__ == "__main__":
    ptb=wrPTB()
    print('PyTechBrain at port: ', ptb.portArduino())
    ptb.blink()

