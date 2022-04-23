import paho.mqtt.client as mqtt

import settings


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(settings.MQTT_TOPIC)
    client.publish(settings.MQTT_TOPIC, "hello from python app")

client = mqtt.Client("python_app")
client.on_connect = on_connect

client.connect(settings.MQTT_SERVER_URL, settings.MQTT_SERVER_PORT, 60)

client.publish("test", "hello from python app")
