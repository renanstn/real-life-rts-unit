#include <WiFi.h>
#include <PubSubClient.h>

const int serialSpeed = 115200;
const char* mqttServer = "0.tcp.ngrok.io";
const int mqttPort = 13791;

WiFiClient espClient;
PubSubClient client(espClient);

void setupWifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin("Wokwi-GUEST", "", 6);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println("Wifi connected!");
}

void mqttCallback(char* topic, byte* payload, unsigned int length) {
  String topic_string(topic);
  Serial.print("Received message in topic: ");
  Serial.print(topic);
  Serial.println();
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
      Serial.print((char) payload[i]);
  }
}

void setupMQTT() {
  client.setServer(mqttServer, mqttPort);
  client.setCallback(mqttCallback);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    String clientId = "ESP32Client-";
    clientId += String(WiFi.macAddress());
    if (client.connect(clientId.c_str(), NULL, NULL)) {
      Serial.println("connected");
      client.subscribe("test");
      Serial.println("Subscribed to 'test' topic");
    } else {
      Serial.print("failed with state: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
  Serial.println("Setup MQTT finished");
}

void setup() {
  Serial.begin(serialSpeed);
  setupWifi();
  setupMQTT();
}

void loop() {
  if (!client.connected()) {
    setupMQTT();
  }
  Serial.print(".");
  client.publish("test", "oieeee");
  delay(2000);
}
