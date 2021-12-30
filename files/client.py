import socket
import threading
import json
from .user import User
from .message import Message
from .channel import Channel
import websocket
import time

class Client():
    def _heartbeat(self, interval, ciao):
        while True:
            time.sleep(interval)
            heartbeatJson = {
                "op":1,
                "d":"null"
            }
            self._send_json_request(self._client, heartbeatJson)

    def __init__(self, token):
        self._client = websocket.WebSocket()
        self._client.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        heartbeat_interval = self._receive_json_request(self._client)["d"]["heartbeat_interval"]
        threading._start_new_thread(self._heartbeat, (heartbeat_interval / 1000, ""))

        print("ready")

        self.token = token

        payload = {
            "op":2,
            "d":{
                "token":self.token,
                "intents":513,
                "properties":{
                    "$os":"linux",
                    "$browser":"chrome",
                    "$device":"pc"
                }
            }
        }
        self._send_json_request(self._client, payload)

    def _send_json_request(self, ws, request):
        ws.send(json.dumps(request))

    def _receive_json_request(self, ws):
        response = ws.recv()
        if response:
            return json.loads(response)

    def getMessage(self):
        event = self._receive_json_request(self._client)
        try:
            if "content" in event["d"]:
                toJson = event["d"]
                author = toJson["author"]
                #print(toJson)
                channel = Channel(toJson["channel_id"], self.token)
                global user
                if "bot" in author:
                    user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], True)
                else:
                    user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], False)
                Messaggio = Message(toJson["id"], toJson["content"], user, toJson["type"], toJson["embeds"], toJson["pinned"], toJson["mentions"], toJson["mention_roles"], toJson["attachments"], toJson["mention_everyone"], toJson["tts"], toJson["timestamp"], toJson["edited_timestamp"], toJson["flags"], toJson["components"], channel, self.token)
                return Messaggio
            else:
                return None
        except Exception:
            return None