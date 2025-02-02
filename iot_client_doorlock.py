import paho.mqtt.client as mqtt
door_requests = {"b'Open'": "Door Opened", "b'Close'":"Door Closed"}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Door_Request")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    req = str(msg.payload)
    print(msg.topic + " " + req)
    if req in door_requests:
        client.publish("Message2Controller", door_requests[req], 2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.connect("localhost", 1883, 60)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()