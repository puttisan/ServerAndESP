#include <ESP8266WiFi.h>
//#include <WiFiServer.h>
//#include <WiFiClient.h>
#include <MicroGear.h>
#include <String.h>


#define APPID   "seniorProject"
#define KEY     "NaQYUjMmG9YCPwo"
#define SECRET  "XqSCXMSKfBvFqHwGXnZUGC224"
#define ALIAS   "client_station"

WiFiClient client;
String send_data;
int timer = 0;
MicroGear microgear(client);


/*=== Variable WiFi Static IP ===*/
//const char* ssid = "NooKy"; // Change your name wifi
//const char* password = "22082527"; // Change your password wifi
//const char* ssid = "Natapong"; // Change your name wifi
//const char* password = "0848109998"; // Change your password wifi
 
//const char* ssid     = "MALABADOR";
//const char* password = "0837501830";
const char* wifi_ip[4] = {"192", "168", "10", "200"}; // Change your ip local network
const char* wifi_subnet[4] = {"255", "255", "255", "0"}; // Change your subnet local network
const char* wifi_gateway[4] = {"192", "168", "10", "1"}; // Change your gateway local network

/*=== WiFiAccessPoint ===*/
const char* ssidAP = "RoomTag1"; // Change your name access point
const char* ssidPass = "gotgotgot"; // Change your password access point
const int channel = 6;



/*=== Variable WebServer ===*/
String get_name; // parameter
String get_value; // value
String get_url; // url parameter + value

/*=== Pin control ===*/
uint8_t pin_1 = 4;
uint8_t pin_2 = 5;


void WiFi_Config() {
 if (WiFi.begin(ssid, password)) {
        WiFi.mode(WIFI_AP_STA);
        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");

        }
    }
  Serial.println();
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}


void WiFi_AP() {
  
  //WiFi.softAP(ssidAP);
  WiFi.softAP(ssidAP, ssidPass,channel);
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
    
    //WiFi.mode(WIFI_AP);
    //ESP.restart();
    microgear.on(MESSAGE,onMsghandler);

    /* Call onFoundgear() when new gear appear */
    microgear.on(PRESENT,onFoundgear);

    /* Call onLostgear() when some gear goes offline */
    microgear.on(ABSENT,onLostgear);

    /* Call onConnected() when NETPIE connection is established */
    microgear.on(CONNECTED,onConnected);
   
    Serial.begin(115200);
    Serial.println("Starting...");
    WiFi_Config();
    microgear.init(KEY,SECRET,ALIAS);
    microgear.connect(APPID);

    WiFi_AP();
    //microgear.subscribe("/data");
//  Serial.begin(115200);
//  pinMode(pin_1, OUTPUT);
//  pinMode(pin_2, OUTPUT);

//  WebServer_Config();
  
}

void loop(void) {

 if (microgear.connected()) {

        /* Call this method regularly otherwise the connection may be lost */
        microgear.loop();
//        if (timer >= 100) {
          Scan_WiFi();
//          timer = 0;
//        } 
//        else timer += 100;
    }
    else {
        Serial.println("connection lost, reconnect...");
        if (timer >= 500) {
            microgear.connect(APPID);
            timer = 0;
        }
        else timer += 100;
    }
    delay(10);

}
/* If a new message arrives, do this */
void onMsghandler(char *topic, uint8_t* msg, unsigned int msglen) {
//    Serial.print("Incoming message --> ");
    msg[msglen] = '\0';
//    Serial.println((char *)msg);
//    Serial.print("Incoming message --> ");
//    Serial.print(topic);
//    Serial.print(" : ");
    char strState[msglen];
    for (int i = 0; i < msglen; i++) {
      strState[i] = (char)msg[i];
      Serial.print((char)msg[i]);
    }
//    Serial.println();
//  
//    String stateStr = String(strState).substring(0, msglen);
//  
//    if (stateStr == "ON") {
//      digitalWrite(D0,HIGH);
//      microgear.chat("/data", "ON");
//    } else if (stateStr == "OFF") {
//      digitalWrite(D0,LOW);
//      microgear.chat("/data", "OFF");
//    }
}

void onFoundgear(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.print("Found new member --> ");
    for (int i=0; i<msglen; i++)
        Serial.print((char)msg[i]);
    Serial.println();  
}

void onLostgear(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.print("Lost member --> ");
    for (int i=0; i<msglen; i++)
        Serial.print((char)msg[i]);
    Serial.println();
}

/* When a microgear is connected, do this */
void onConnected(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.println("Connected to NETPIE...");
    /* Set the alias of this microgear ALIAS */
    microgear.setName(ALIAS);
    
}

//convert string to hex for macAddress
String conv_to_hex(String conv_data){
  char conv_data2[2];
  strcpy(conv_data2, conv_data.c_str());
  int conv_data3 = atoi(conv_data2);
  char hex[20];
  sprintf(hex,"%02X",conv_data3);
  return hex;
}

/*Scan WiFi and return String*/
void Scan_WiFi(){
  String data;
//  Serial.println("scan start");

  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
//  Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
//    Serial.print(n);
//    Serial.println(" networks found");
    //start
    microgear.publish("/Station_data/1","<");
    for (int i = 0; i < n; ++i)
    {
      
      data = "";
      // Print SSID and RSSI for each network found
//      Serial.print(i + 1);
//      Serial.print(": ");
//      Serial.print(WiFi.SSID(i));
//      Serial.print(" (");
//      Serial.print(WiFi.RSSI(i));
//      Serial.print(")");
//      Serial.print("macAddress:");
//      Serial.print(WiFi.BSSID(i)[0],HEX);
//      Serial.print(":");
//      Serial.print(WiFi.BSSID(i)[1],HEX);
//      Serial.print(":");
//      Serial.print(WiFi.BSSID(i)[2],HEX);
//      Serial.print(":");
//      Serial.print(WiFi.BSSID(i)[3],HEX);
//      Serial.print(":");
//      Serial.print(WiFi.BSSID(i)[4],HEX);
//      Serial.print(":");
//      Serial.print(WiFi.BSSID(i)[5],HEX);
//      Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE)?" ":"*");

      data = data+WiFi.SSID(i) + ",";
      String conv;
      for (int j = 0; j < 6; ++j)
      {
        conv = (WiFi.BSSID(i)[j]);
        data = data + conv_to_hex(conv);
      }
      data = data + "," + WiFi.RSSI(i);
      microgear.publish("/Station_data/1",data);
      delay(20);
    }
  }
  //end
  microgear.publish("/Station_data/1",">");
//  Serial.println("");
}
