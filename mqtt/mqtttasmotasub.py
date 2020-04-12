# MQTT Client demo
# Continuosly monitor two different MQTT topics for data,
# check if the received data matches two predefined 'command'

import paho.mqtt.client as mqtt

# The callback for when the client recives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Command with result code " + str(rc))

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscription will be renewed.
    client.subscribe("cmnd/tasmota/light_D8DF25/power1")
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(type(msg.payload))

    if msg.payload == b"Hello":
        print("Received message #1, do something")

    if msg.payload == b"World!":
        print("Received #2")

# Create an MQTT client and attach our routine to it.
mqtt = mqtt.Client(userdata="tom")
mqtt.username_pw_set("alto","Ihm$2Te0T")
mqtt.on_connect = on_connect
mqtt.on_message = on_message
mqtt.connect_async(host="192.168.1.127",port=1883)

# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions

# mqtt.loop_start()
mqtt.loop_forever()
