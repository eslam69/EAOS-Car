import urllib.request
import time

root_url = "http://192.168.4.1/"  
# root_url = "http://192.168.43.224/"  

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP
def sendMessage(server_base_ip,content):
	url_content = server_base_ip+ "?State=" +content 
	n = urllib.request.urlopen(url_content) # send request to ESP

if __name__ == "__main__":
	
	while True:
		answer = input(""" direction: """).upper()
		print(root_url+answer)
		
		# try:
		# 	sendRequest(root_url+"?State="+answer)
		# 	print("SENT!\n\n")
		# except :
		# 	print("ERROR")
		sendRequest(root_url+"?State="+answer)
		time.sleep(0.4)
		sendRequest(root_url+"?State="+"S")
		print("SENT!\n\n")
		