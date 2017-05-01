import sys
import instance

while 1:

    try:

        print 'Water:' + instance.do_scale(27, 17, 1)
        print 'Food:' + instance.do_scale(26, 19, 1)

    except KeyboardInterrupt:
        sys.exit()
