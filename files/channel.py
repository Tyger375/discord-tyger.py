import requests
import json
import message as Message
from user import User

class Channel():
    def __init__(self, id, token):
        self.id = id
        self._token = token

    async def send(self, message, embeds=[]):
        newEmbeds = []
        for embed in embeds:
            newEmbeds.append(embed.to_dict())
        data = {
            "content":message,
            "embeds":newEmbeds
        }
        headers = {
            "Content-Type":"application/json",
            "Authorization":"Bot " + self._token
        }
        response = requests.post(
            "https://discord.com/api/channels/" + str(self.id) + "/messages", 
            data=json.dumps(data),
            params={"wait":True},
            headers=headers
        )
        toJson = response.json()
        author = toJson["author"]
        channel = Channel(toJson["channel_id"], self._token)
        global user
        if "bot" in author:
            user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], True)
        else:
            user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], False)
        Messaggio = Message.Message(toJson["id"], toJson["content"], user, toJson["type"], toJson["embeds"], toJson["pinned"], toJson["mentions"], toJson["mention_roles"], toJson["attachments"], toJson["mention_everyone"], toJson["tts"], toJson["timestamp"], toJson["edited_timestamp"], toJson["flags"], toJson["components"], channel, self._token)
        return Messaggio