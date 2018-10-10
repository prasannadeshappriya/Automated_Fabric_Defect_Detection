from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.preview_fullscreen=False
camera.preview_window=(620, 320, 640, 480)
camera.start_preview()
sleep(13)
camera.stop_preview()

class Camera:
    camera=''
    
    def __init__(self):
        Camera.camera = PiCamera()
        Camera.camera.preview_fullscreen=False
        Camera.camera.awb_mode = 'off'
        Camera.camera.awb_gains = (1.0,1.0)
        Camera.camera.preview_window=(620, 320, 640, 480)

    def capture(self,folder_name,filename,sleep_time):
        Camera.camera.start_preview()
        sleep(sleep_time)#20
        Camera.camera.capture('/home/pi/Desktop/FYP/Automated_Fabric_Defect_Detection/Defect Capture/' + str(folder_name) + '/'+ str(filename)+'.jpg')
        Camera.camera.stop_preview()

    def preview(self,sleep_time):
        Camera.camera.start_preview()
        sleep(20)
        Camera.camera.stop_preview()

            
