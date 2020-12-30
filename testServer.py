import requests

def test_post_direction():
    url = 'http://192.168.1.6:5000/direction'
    myobj = 'R'

    x = requests.post(url, data = myobj)

    # print(x.text)
def test_post_file():
    url = 'http://192.168.1.6:5000/frame'
    myobj = {'image': open('Data/road3.jpg', 'rb')}
    x = requests.post(url, files = myobj)

test_post_file()