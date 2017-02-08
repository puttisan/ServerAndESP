
#include <ESP8266WiFi.h>
#include <MicroGear.h>


//const char* ssid     = "MALABADOR";
//const char* password = "0837501830";

const char* ssid     = "SRISUNUN 01(2.4G)";
const char* password = "30007000";


#define APPID   "seniorProject"
#define KEY     "pv9rNyJv3sbObxm"
#define SECRET  "adXBMFdIAmLh56UUl2oduZetu"
#define ALIAS   "client_Tag_control"
WiFiClient client;

String send_data;
int timer = 0;
MicroGear microgear(client);
int countON = 0;
int countOFF = 0;

const uint8_t output = D2;

void onControl(int number,String order){
//  Serial.print(number);
//  Serial.print(" ");
//  Serial.print(order);
//  String str = itoa(number);
//  sprintf(str, "%d", number);
  String send_Txt = String(number) + "->" + order;
//  strcat(send_Txt,number);
//  strcat(send_Txt,"->");
//  strcat(send_Txt,order);
  if((number == 1)&&(order == "ON")){
     if(countON>=2){
       digitalWrite(output,HIGH);
       countOFF = 0;
       microgear.publish("/dataControl",send_Txt); 
       Serial.println(send_Txt);
       Serial.println(countON);
       
     }
     else{countON++;}  
  }
  else if((number == 1)&&(order == "OFF")){
    if(countOFF>=3){
       digitalWrite(output,LOW);
       countON = 0;
       microgear.publish("/dataControl",send_Txt);
       Serial.println(send_Txt);
       Serial.println(countOFF); 
     }
     else{countOFF++;}  
  }
  
}
/* If a new message arrives, do this */
void onMsghandler(char *topic, uint8_t* msg, unsigned int msglen) {
// Serial.print("Incoming message --> ");
   
    msg[msglen] = '\0';
//    Serial.println((char *)msg);
//    Serial.print("Incoming message --> ");
//    Serial.print(topic);
//    Serial.print(" : ");
    char strState[msglen];
    for (int i = 0; i < msglen; i++) {
      strState[i] = (char)msg[i];
//      Serial.print((char)msg[i]);
    }
//    Serial.println();
  
    String stateStr = String(strState).substring(0, msglen);
//    Serial.print(stateStr);
//    char * str_temp = strchr(stateStr,3);
//    char * pch; 
    String pch = stateStr.substring(0, 1);
    String pch2 = stateStr.substring(2);
//    Serial.print(pch); 
//    Serial.print("\n");
//    Serial.print(pch2); 
    onControl(pch.toInt(),pch2);
//    if (stateStr == "ON") {
//      digitalWrite(D0,HIGH);
//      microgear.chat("/data", "ON");
//    } else if (stateStr == "OFF") {
//      digitalWrite(D0,LOW);
//      microgear.chat("/data", "OFF");
//    }
///////////////////////////////////////////////////////////////////////
//    Serial.print("Incoming message --> ");
//    msg[msglen] = '\0';
//    Serial.println((char *)msg);
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

void setup() {
    pinMode(output,OUTPUT);
  
    microgear.on(MESSAGE,onMsghandler);
    microgear.on(PRESENT,onFoundgear);
    microgear.on(ABSENT,onLostgear);
    microgear.on(CONNECTED,onConnected);
    Serial.begin(115200);
    Serial.println("Starting...");
    if (WiFi.begin(ssid, password)) {
        WiFi.mode(WIFI_STA);
        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
        }
    }
    Serial.println("WiFi connected");  
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    microgear.init(KEY,SECRET,ALIAS);
    microgear.connect(APPID);
//    microgear.subscribe("/dataControl");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (microgear.connected()) {

        /* Call this method regularly otherwise the connection may be lost */
        microgear.loop();
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
