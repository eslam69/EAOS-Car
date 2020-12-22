import urllib.request

root_url = "http://192.168.1.8/"  

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP
def sendMessage(server_base_ip,content):
	url_content = server_base_ip+content 
	n = urllib.request.urlopen(url_content) # send request to ESP

if __name__ == "__main__":
	
	while True:
		answer = input(""" To control the led, type "ON" or "OFF": """).upper()
		if (answer=="ON"):
			sendRequest(root_url+"/LED=ON")
			print("Opened!\n\n")
		if (answer=="OFF"):
			sendRequest(root_url+"/LED=OFF")
			print("Closed!\n\n")