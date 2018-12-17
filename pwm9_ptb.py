from wrPTB import *

b = wrPTB()
print('PyTechBrain at port: ', b.portArduino())
print('Press Ctrl+C to Exit')
while True:
    try:
        b.pwm9(pwm=255)
        b.sleep(1)
        for i in range(256):
            b.pwm9(pwm=255-i)
        
    except (KeyboardInterrupt, SystemExit):
        b.pwm9()
        b.exit()

