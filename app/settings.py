from decouple import config


MQTT_SERVER_URL = config("MQTT_SERVER_URL")
MQTT_SERVER_PORT = config("MQTT_SERVER_PORT")
MQTT_TOPIC = config("MQTT_TOPIC")
