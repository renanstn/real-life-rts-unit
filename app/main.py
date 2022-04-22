import paho.mqtt.client as mqtt

import settings


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(settings.MQTT_TOPIC)
    client.publish(settings.MQTT_TOPIC, "hello from python app")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client("python_app")
client.on_connect = on_connect
client.on_message = on_message

client.connect(settings.MQTT_SERVER_URL, settings.MQTT_SERVER_PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
