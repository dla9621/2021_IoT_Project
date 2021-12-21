import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()
now_str = time.strftime("%Y%m%d_%H%M%S")

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    while True:
        val = input('photo : 1, video : 2, exit : 9 > ')
        if val == '1':
            print('사진 촬영')
            time.sleep(3)
            camera.capture('%s/%s.jpg' % (path, now_str))
        elif val == '2':
            print('동영상 촬영')
            time.sleep(3)
            camera.start_recording('%s/%s.h264' % (path, now_str))
            time.sleep(1)
            camera.stop_recording()
        elif val == '9':
            break
        else:
            print('incorrect command')

finally:
    camera.stop_preview()