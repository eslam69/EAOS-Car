#include <ESP8266WiFi.h>
 
const char* ssid = "Eslam";
const char* password = "01006497889";
 
int ledPin = 13; // GPIO13
WiFiServer server(80);
 
void setup() {
  Serial.begin(115200);
  delay(10);
 
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
 
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
 
}
 
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
 
  // Match the request
 
  int value = LOW;
  if (request.indexOf("/right") != -1)  {
    //write motor right_dir configs here
    digitalWrite(ledPin, HIGH);
    Serial.println("go right");
    value = HIGH;
  }
  if (request.indexOf("/left") != -1)  {
    //write motor forward_dir configs here
    digitalWrite(ledPin, LOW);
    Serial.println("go left");
    value = LOW;
  }

  if (request.indexOf("/forward") != -1)  {
    //write motor forward_dir configs here
    digitalWrite(ledPin, LOW);
    Serial.println("go forward");
    value = LOW;
  }

  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
 
}
 
