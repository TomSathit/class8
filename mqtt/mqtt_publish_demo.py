# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
publish.single("Alto/class8/test", "sathit s.", hostname="test.mosquitto.org")