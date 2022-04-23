import paho.mqtt.client as mqtt

import settings


def mqtt_publish_message(topic: str, message: str):
    client = mqtt.Client("python_app")
    client.connect(settings.MQTT_SERVER_URL, settings.MQTT_SERVER_PORT, 60)
    client.publish(topic, message)
