from core import *
from ESP.esp_python_client import *
import time

ESP_SERVER_IP = "http://192.168.1.6/"  # Eslam Home


# ESP_SERVER_IP =  "http://192.168.4.1/"  #IN case of ESP hotspot


if __name__ == "__main__":

    time.sleep(2)
    # print("Connected to camera")
    sleepTime = {"F": 0.3, "R": 0.05, "L": 0.05, "S": 0.1}
    while True:
        imgResp = urllib.request.urlopen('http://192.168.1.4:8080/shot.jpg')

        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

        #decode the array to OpenCV usable format
        frame = cv2.imdecode(imgNp, -1)
        direction = compute_direction(frame)
        print(direction)
        test_photo(frame)
# ---------------------------------------------------------------------------- #
        #move, wait, stop
        sendMessage(ESP_SERVER_IP, direction)
        time.sleep(sleepTime.get(direction,1))
        sendMessage(ESP_SERVER_IP, "S")
        time.sleep(0.2)

# ---------------------------------------------------------------------------- #
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
