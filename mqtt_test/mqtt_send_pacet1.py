import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = uniform(20, 21)
    client.publish("TEMPERATURE", randNumber)
    print("Published :" +str(randNumber)+" to topic Temperature_Inside")
    time.sleep(1)
