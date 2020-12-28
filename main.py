from core import *
from ESP.esp_python_client import *
import time

# ESP_SERVER_IP = "http://192.168.1.8/"  #Eslam Home


ESP_SERVER_IP =  "http://192.168.4.1/"  #IN case of ESP hotspot


if __name__ == "__main__":
    # capture = cv2.VideoCapture(CAMERA_IP)
    capture = cv2.VideoCapture("http://192.168.4.3:8080/video")
    while True:
        ret, frame = capture.read()
        # print(image.shape)
        # cv2.imshow("Test", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # test_photo('data/road3.jpg')
        direction = compute_direction(frame)
        print(direction)
# ---------------------------------------------------------------------------- # 
        #move, wait, stop
        sendMessage(ESP_SERVER_IP, direction)
        time.sleep(0.4)
        sendMessage(ESP_SERVER_IP, "S")
# ---------------------------------------------------------------------------- #
        test_photo(frame)

    cv2.destroyAllWindows()
