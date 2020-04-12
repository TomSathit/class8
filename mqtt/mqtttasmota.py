import paho.mqtt.client as mqtt
import time
# def on_connect(client, userdata, flags, rc):
#     print("Command with result code " + str(rc))
#
#     # Subscribing in on_connect() - if we lose the connection and
#     # reconnect then subscription will be renewed.
#     client.subscribe("Alto/test")
#     client.subscribe("Alto/devices")
#
# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic + " " + str(msg.payload))
#     print(type(msg.payload))
#
#     if msg.payload == b"Hello":
#         print("Received message #1, do something")
#
#     if msg.payload == b"World!":
#         print("Received #2")

mqtt = mqtt.Client(userdata="alto")
mqtt.username_pw_set("alto","Ihm$2Te0T")
# mqtt.on_connect = on_connect
# mqtt.on_message = on_message
mqtt.connect_async(host="192.168.1.127",port=1883)
mqtt.loop_start()

print("saas")
while True:
    time.sleep(3)
    status = "off"
    topic = "cmnd/tasmota/light_D8DF25/power0"
    mqtt.publish(topic=topic,payload=status)
    topic = "cmnd/tasmota/light_D8DF25/power1"
    mqtt.publish(topic=topic,payload=status)
    topic = "cmnd/tasmota/light_D8DF25/power2"
    mqtt.publish(topic=topic,payload=status)
    time.sleep(3)
    status = "on"
    topic = "cmnd/tasmota/light_D8DF25/power0"
    mqtt.publish(topic=topic,payload=status)
    topic = "cmnd/tasmota/light_D8DF25/power1"
    mqtt.publish(topic=topic,payload=status)
    topic = "cmnd/tasmota/light_D8DF25/power2"
    mqtt.publish(topic=topic,payload=status)