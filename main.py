from core import *
from ESP.esp_python_client import *

ESP_SERVER_IP = "http://192.168.1.8/"

if __name__ == "__main__":
    capture = cv2.VideoCapture(CAMERA_IP)
    while True:
        ret, frame = capture.read()
        # print(image.shape)
        # cv2.imshow("Test", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # test_photo('data/road3.jpg')
        direction = compute_direction(frame)
        print(direction)
        sendMessage(ESP_SERVER_IP, direction)
        test_photo(frame)

    cv2.destroyAllWindows()
