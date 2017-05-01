import sys
import instance
import time

while 1:

    try:

        print 'Water:' + str(instance.do_scale(27, 17, 1))
        time.sleep(.5)
        print 'Food:' + str(instance.do_scale(26, 19, 1))
        time.sleep(.5)

    except KeyboardInterrupt:
        sys.exit()
