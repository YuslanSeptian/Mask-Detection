import cv2 
import yolov5-master.detect
import os

video_capture = cv2.VideoCapture(0)
detect_api = yolov5-master.detect.DetectAPI(exist_ok=True)

while True:
	k = cv2.waitKey(1)
    ret, frame = video_capture.read()
    
    path = 'Your catalog/yolov5-master/data/myimages'
    cv2.imwrite(os.path.join(path, 'test.jpg'), frame)
    
    label = detect_api.run()
    print(str(label))
    
    image = cv2.imread('Your catalog/yolov5-master/runs/detect/myexp/test.jpg', flags=1)
    cv2.imshow("video", image)

    if k == 27:  # Press ESC to exit the window
        break

video_capture.release()
