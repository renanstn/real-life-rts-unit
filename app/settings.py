from decouple import config


MQTT_SERVER_URL = config("MQTT_SERVER_URL")
MQTT_SERVER_PORT = config("MQTT_SERVER_PORT", cast=int)
MQTT_TOPIC = config("MQTT_TOPIC")

WEBCAM_URL = config("WEBCAM_URL")
