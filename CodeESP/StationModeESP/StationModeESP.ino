#include <ESP8266WiFi.h>
#include <WiFiServer.h>
#include <WiFiClient.h>
//#include <ESP8266WebServer.h>
//#include <AsciiToString.h>

#define MAX_CLIENTS 1 // MAX Telnet client

/*=== Variable WiFi Static IP ===*/
const char* ssid = "NooKy"; // Change your name wifi
const char* password = "22082527"; // Change your password wifi
const char* wifi_ip[4] = {"192", "168", "10", "200"}; // Change your ip local network
const char* wifi_subnet[4] = {"255", "255", "255", "0"}; // Change your subnet local network
const char* wifi_gateway[4] = {"192", "168", "10", "1"}; // Change your gateway local network

/*=== WiFiAccessPoint ===*/
const char* ssidAP = "ESP_AP"; // Change your name access point
const char* ssidPass = "gotgotgot"; // Change your password access point

/*=== Variable WebServer ===*/
String get_name; // parameter
String get_value; // value
String get_url; // url parameter + value

/*=== Pin control ===*/
uint8_t pin_1 = 4;
uint8_t pin_2 = 5;

//AsciiToString ascii_str; // Libraries Convert ascii code to string
//WiFiServer server_telnet(23);
//WiFiClient serverClients[MAX_CLIENTS];

//ESP8266WebServer server(80);

void WiFi_Config() {
  WiFi.begin(ssid, password);

  /*=== If you not use static ip comment here ===*/
//  WiFi.config(
//    IPAddress(atoi(wifi_ip[0]), atoi(wifi_ip[1]), atoi(wifi_ip[2]), atoi(wifi_ip[3])),
//    IPAddress(atoi(wifi_gateway[0]), atoi(wifi_gateway[1]), atoi(wifi_gateway[2]), atoi(wifi_gateway[3])),
//    IPAddress(atoi(wifi_subnet[0]), atoi(wifi_subnet[1]), atoi(wifi_subnet[2]), atoi(wifi_subnet[3]))
//  );
  /*=== End comment here ===*/
  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

///*=== TELNET ===*/
//void telnet_server() {
//
//  uint8_t i;
//  server_telnet.begin();
//  server_telnet.setNoDelay(true);
//
//  if (server_telnet.hasClient()) {
//    for (i = 0; i < MAX_CLIENTS; i++) {
//      if (!serverClients[i].connected()) {
//        if (serverClients[i]) {
//          serverClients[i].stop();
//        }
//        serverClients[i] = server_telnet.available();
//        Serial.print("Telnet client id : ");
//        Serial.print(i);
//      }
//    }
//    Serial.println();
//  }
//
//  for (i = 0; i < MAX_CLIENTS; i++) {
//    if (serverClients[i].connected()) {
//      while (serverClients[i].available()) {
//        
//        ascii_str.getString(serverClients[i].read());
//
//        /*=== funtion ascii_str.message you can set message for control ===*/
//        if (ascii_str.message == "00") {
//
//          Serial.println("TELNET RELAY_1 : OFF");
//          digitalWrite(pin_1, HIGH);
//          ascii_str.clear();
//
//        } else if (ascii_str.message == "01") {
//
//          Serial.println("TELNET RELAY_1 : ON");
//          digitalWrite(pin_1, LOW);
//          ascii_str.clear();
//
//        } else if (ascii_str.message == "10") {
//
//          Serial.println("TELNET RELAY_2 : OFF");
//          digitalWrite(pin_2, HIGH);
//          ascii_str.clear();
//        } else if (ascii_str.message == "11") {
//  
//            Serial.println("TELNET RELAY_2 : ON");
//            digitalWrite(pin_2, LOW);
//            ascii_str.clear();
//        }
//        
//      }
//    }
//  }
//
//}/*===== END TELNET =====*/
//
//void WebServer_Config() {
//  
//  server.on("/", webserver_display);
//  server.begin();
//  Serial.println("HTTP server started");
//  
//}

//void webserver_display() {
//  
//  server.send(200, "text/html", "WAITING HTTP GET / TELNET TCP ...");
//  get_name = server.argName(0);
//  get_value = server.arg(0);
//  get_url = get_name;
//  get_url += ":";
//  get_url += get_value;
//
//  if (get_url == "relay:00") {
//    
//    digitalWrite(pin_1, HIGH);
//    Serial.println("HTTP GET RELAY_1 : OFF");
//    
//  } else if (get_url == "relay:01") {
//    
//    digitalWrite(pin_1, LOW);
//    Serial.println("HTTP GET RELAY_1 : ON");
//    
//  } else if (get_url == "relay:10") {
//    
//    digitalWrite(pin_2, HIGH);
//    Serial.println("HTTP GET RELAY_2 : OFF");
//    
//  } else if (get_url == "relay:11") {
//    
//    digitalWrite(pin_2, LOW);
//    Serial.println("HTTP GET RELAY_2 : ON");
//    
//  }
//  
//}

void WiFi_AP() {
  
  //WiFi.softAP(ssidAP);
  
  /*=== If you need password wifi remove comment ===*/
  WiFi.softAP(ssidAP, ssidPass);
  
  Serial.print("WiFi AP : ");
  Serial.print(ssidAP);
  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  
  Serial.println();
  Serial.println("WiFi AP Success");
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  
}

void setup(void) {
  
  Serial.begin(115200);
//  pinMode(pin_1, OUTPUT);
//  pinMode(pin_2, OUTPUT);
  WiFi_Config();
  WiFi_AP();
//  WebServer_Config();
  
}

void loop(void) {

//  server.handleClient();
//  telnet_server();
  delay(500);

}
