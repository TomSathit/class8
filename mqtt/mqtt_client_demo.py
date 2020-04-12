# MQTT Client demo
# Continuosly monitor two different MQTT topics for data,
# check if the received data matches two predefined 'command'

import paho.mqtt.client as mqtt

# The callback for when the client recives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Command with result code " + str(rc))

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscription will be renewed.
    client.subscribe("Alto/test")
    client.subscribe("Alto/devices")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(type(msg.payload))

    if msg.payload == b"Hello":
        print("Received message #1, do something")

    if msg.payload == b"World!":
        print("Received #2")

# Create an MQTT client and attach our routine to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions

client.loop_forever()
