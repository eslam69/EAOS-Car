
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
 
const char* ssid = "Eslam";
const char* password = "01006497889";
 
void setup () {
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.print("Connecting..");
 
  }
 
}
void Move()
{
 HTTPClient httpDirection;  //Declare an object of class HTTPClient
 
    httpDirection.begin("http://192.168.1.6:5000/direction");  //Specify request destination
    int directionMessage = httpDirection.GET();                                  //Send the request
 
    if (directionMessage > 0) { //Check the returning code  
      String command = httpDirection.getString();   //Get the request response payload
      Serial.println(command);             //Print the response payload
      if (command == "F") goAhead();
      else if (command == "B") goBack();
      else if (command == "L") goLeft();
      else if (command == "R") goRight();
      else if (command == "I") goAheadRight();
      else if (command == "G") goAheadLeft();
      else if (command == "J") goBackRight();
      else if (command == "H") goBackLeft();
      else if (command == "0") speedCar = 400;
      else if (command == "1") speedCar = 470;
      else if (command == "2") speedCar = 540;
      else if (command == "3") speedCar = 610;
      else if (command == "4") speedCar = 680;
      else if (command == "5") speedCar = 750;
      else if (command == "6") speedCar = 820;
      else if (command == "7") speedCar = 890;
      else if (command == "8") speedCar = 960;
      else if (command == "9") speedCar = 1023;
      else if (command == "S") stopRobot();
    }
    
    }
} 
void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient httpState;  //Declare an object of class HTTPClient
 
    httpState.begin("http://192.168.1.6:5000/state");  //Specify request destination
    int stateMessage = httpState.GET();                                  //Send the request
 
    if (stateMessage > 0) { //Check the returning code
 
      String payload = httpState.getString();   //Get the request response payload
      Serial.println(payload);             //Print the response payload
      if ( payload == "done")
      {
        Move();
        httpState.POST("done");
      }
 
    }
 
    http.end();   //Close connection
 
  }
 
  delay(200);    //Send a request every 30 seconds
}
