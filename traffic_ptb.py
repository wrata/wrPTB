from wrPTB import *

b=wrPTB()
print('PyTechBrain at port: ', b.portArduino())
print('Press Ctrl+C to Exit')
while True:
    try:
        b.traffic(R=1)
        b.sleep(3)
        b.traffic(R=1, Y=1)
        b.sleep(1)
        b.traffic(G=1)
        b.sleep(3)
        b.traffic(Y=1)
        b.sleep(1)      
    except (KeyboardInterrupt, SystemExit):
        b.traffic()
        b.exit()

