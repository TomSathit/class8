import paho.mqtt.client as mqtt
import time

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
    