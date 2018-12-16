from wrPTB import *

b = wrPTB()
print('PyTechBrain at port: ', b.portArduino())
print('Press Ctrl+C to Exit')
while True:
    try:
        b.rgb(R=255)
        print('red')
        b.sleep(2)
        
        b.rgb(G=255)
        print('green')
        b.sleep(2)
        
        b.rgb(B=255)
        print('blue')
        b.sleep(2)
        
        b.rgb(R=255, G=255, B=255)
        print('white')
        b.sleep(2)

        b.rgb(R=255, G=255)
        print('yellow')
        b.sleep(2)

        b.rgb(G=255, B=255)
        print('cyan')
        b.sleep(2)

        b.rgb(R=255, B=255)
        print('magenta')
        b.sleep(2)
        
    except (KeyboardInterrupt, SystemExit):
        b.rgb()
        b.exit()

