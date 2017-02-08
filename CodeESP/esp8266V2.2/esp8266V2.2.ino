/*  NETPIE ESP8266 basic sample                            */
/*  More information visit : https://netpie.io             */

#include <ESP8266WiFi.h>
#include <MicroGear.h>
#include <String.h>
#include <time.h>
//
//const char* ssid     = "NooKy";
//const char* password = "22082527";
int timezone = 7 * 3600;                    //ตั้งค่า TimeZone ตามเวลาประเทศไทย
int dst = 0; 
//const char* ssid     = "Natapong";
//const char* password = "0848109998";

//
//const char* ssid     = "SRISUNUN 01(2.4G)";
//const char* password = "30007000";
//
const char* ssid     = "MALABADOR";
const char* password = "0837501830";

#define APPID   "seniorProject"
#define KEY     "0sEvbvtdC5vdWha"
#define SECRET  "enEvPI5j4AV2JerNEQYbRSRrC"
#define ALIAS   "esp8266"

WiFiClient client;

/*String for send microgear*/
String send_data;
int timer = 0;
MicroGear microgear(client);


/* If a new message arrives, do this */
void onMsghandler(char *topic, uint8_t* msg, unsigned int msglen) {
    Serial.print("Incoming message --> ");
    msg[msglen] = '\0';
    Serial.println((char *)msg);
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

//   WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
//  Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
//    Serial.print(n);
//    Serial.println(" networks found");
    //start
    microgear.publish("/data/1","<");
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
      microgear.publish("/data/1",data);
//      delay(20);
    }
  }
  //end
  microgear.publish("/data/1",">");
//  Serial.println("");
}


void setup() {
    /* Add Event listeners */
    /* Call onMsghandler() when new message arraives */
   // ESP.wdtEnable(15000); // make the watch dog timeout longer
//    ESP.wdtDisable();
   // delay(10000);         // long delay

    
    microgear.on(MESSAGE,onMsghandler);

    /* Call onFoundgear() when new gear appear */
    microgear.on(PRESENT,onFoundgear);

    /* Call onLostgear() when some gear goes offline */
    microgear.on(ABSENT,onLostgear);

    /* Call onConnected() when NETPIE connection is established */
    microgear.on(CONNECTED,onConnected);

    Serial.begin(115200);
    Serial.println("Starting...");
    //ESP.wdtDisable();
    /* Initial WIFI, this is just a basic method to configure WIFI on ESP8266.                       */
    /* You may want to use other method that is more complicated, but provide better user experience */
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
//    configTime(timezone, dst, "pool.ntp.org", "time.nist.gov");     //ดึงเวลาจาก Server
//    Serial.println("\nWaiting for time");
//    while (!time(nullptr)) {
//      Serial.print(".");
//      delay(1000);
//    }
//    /* Initial with KEY, SECRET and also set the ALIAS here */
    microgear.init(KEY,SECRET,ALIAS);

    /* connect to NETPIE to a specific APPID */
    microgear.connect(APPID);
    //microgear.subscribe("/data");
}

void loop() {
    /* To check if the microgear is still connected */
    if (microgear.connected()) {

        /* Call this method regularly otherwise the connection may be lost */
        microgear.loop();
//        if (timer >= 100) {
          Scan_WiFi();
//          configTime(timezone, dst, "pool.ntp.org", "time.nist.gov");    //ดีงเวลาปัจจุบันจาก Server อีกครั้ง
//          time_t now = time(nullptr);
//          struct tm* p_tm = localtime(&now);
//          delay(1000);
//          Serial.print(p_tm->tm_hour);
//           Serial.println("");
          //microgear.publish("/data",send_data);
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
    
//    delay(10);
}
