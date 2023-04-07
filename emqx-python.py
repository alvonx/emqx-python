import json
import random
import time

from paho.mqtt import client as mqtt_client

BROKER = '<server-ip>'
# PORT = 1883
PORT = <port2> # read README.md

# TOPIC = " SUBCRIBE AND PUBLISH TO AN EMQX-MQTT BROKER "
TOPIC = ["<topic-name>"]
# generate client ID with pub prefix randomly
CLIENT_ID = "python-mqtt-tcp-pub-{id}".format(id=random.randint(0, 1000))

USERNAME = '<user-name created>'
PASSWORD = '<user-password>'

FLAG_CONNECTED = 0


def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    if rc == 0:
        FLAG_CONNECTED = 1
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code {rc}".format(rc=rc), )


def connect_mqtt():
    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def publish(client):
    msg_count = 0
    while True:
        msg_dict = {
            'msg': msg_count
        }
        msg = json.dumps(msg_dict)
        topic_name = TOPIC[random.randint(0, len(TOPIC)-1)]
        print(topic_name)
        result = client.publish(topic_name, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Sent `{msg}` to topic `{topic}`".format(msg=msg, topic=topic_name))
        else:
            print("Failed to send message to topic {topic}".format(topic=topic_name))
        msg_count += 1
        time.sleep(random.randint(1, 4))


def run():
    client = connect_mqtt()
    client.loop_start()
    time.sleep(random.randint(1, 4))
    if FLAG_CONNECTED:
        publish(client)
    else:
        client.loop_stop()


if __name__ == '__main__':
    run()
