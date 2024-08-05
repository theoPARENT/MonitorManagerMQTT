from paho.mqtt import client as mqtt

import json
import os

# Load environment variables from .env file
with open('.env.local') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
        client.subscribe(os.getenv('TOPIC'))
    else:
        print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    result = json.loads(msg.payload)
    os.system(os.getenv('APP_PATH') + ' -load:' + os.getenv('PROFILE_PATH') + result['profile'] + '.xml')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.username_pw_set(os.getenv('MQTT_USERNAME'), os.getenv('MQTT_PASSWORD'))
    client.connect(os.getenv('MQTT_BROKER'), 1883, 60)
except Exception as e:
    print(e)

client.loop_forever()
