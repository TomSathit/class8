# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("Alto/test", "Hello", hostname="test.mosquitto.org")
publish.single("Alto/devices", "World!", hostname="test.mosquitto.org")