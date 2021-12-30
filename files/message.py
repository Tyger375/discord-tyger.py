import requests
import json as JSON
from embed import Embed
from channel import Channel
from user import User

class Message():
    def _transform_embeds(self, embeds):
        EMBEDS = []
        for embed in embeds:
            newEmbed = Embed(title=embed["title"], description=embed["description"], color=embed["color"])
            for field in embed["fields"]:
                newEmbed.add_field(name=field["name"], value=field["value"], inline=field["inline"])
            EMBEDS.append(newEmbed)
        self.embeds = EMBEDS
    def __init__(self,
                    id,
                    content,
                    author,
                    type,
                    embeds,
                    pinned,
                    mentions,
                    mention_roles,
                    attachments,
                    mention_everyone,
                    tts,
                    timestamp,
                    edited_timestamp,
                    flags,
                    components,
                    channel,
                    token
                    ):
        self.id = id
        self.content = content
        self.author = author
        self.type = type
        
        self._transform_embeds(embeds)
        #self.embeds = embeds
        self.pinned = pinned
        self.mentions = mentions
        self.mention_roles = mention_roles
        self.attachments = attachments
        self.mention_everyone = mention_everyone
        self.tts = tts
        self.timestamp = timestamp
        self.edited_timestamp = edited_timestamp
        self.flags = flags
        self.components = components
        self.channel = channel
        self._token = token
        self._headers = {
            "Content-Type":"application/json",
            "Authorization":"Bot " + self._token
        }

    def __repr__(self):
        return str(self.to_dict())
        #return f"<DiscordMessage {self.id}>"

    async def edit(self, content=None, embeds=None):
        global newContent, newEmbeds1
        newContent = content
        newEmbeds1 = embeds
        if content == None:
            newContent = self.content
        if embeds == None:
            newEmbeds1 = self.embeds
        newEmbeds = []
        for embed in newEmbeds1:
            newEmbeds.append(embed.to_dict())
        data = {
            "content":newContent,
            "embeds":newEmbeds
        }
        richiesta = requests.patch(
            f"https://discord.com/api/channels/{self.channel.id}/messages/{self.id}",
            data=JSON.dumps(data),
            params={"wait":True},
            headers=self._headers
        )
        toJson = richiesta.json()
        author = toJson["author"]
        #print(toJson)
        channel = Channel(toJson["channel_id"], self._token)
        global user
        if "bot" in author:
            user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], True)
        else:
            user = User(author["username"], author["id"], author["discriminator"], author["avatar"], author["public_flags"], False)
        Messaggio = Message(toJson["id"], toJson["content"], user, toJson["type"], toJson["embeds"], toJson["pinned"], toJson["mentions"], toJson["mention_roles"], toJson["attachments"], toJson["mention_everyone"], toJson["tts"], toJson["timestamp"], toJson["edited_timestamp"], toJson["flags"], toJson["components"], channel, self._token)
        return Messaggio


    async def delete(self):
        richiesta = requests.delete(
            f"https://discord.com/api/channels/{self.channel.id}/messages/{self.id}", headers=self._headers
        )
        return richiesta

    def to_dict(self):
        Obj = {
            "id": self.id,
            "content":self.content,
            "type":self.type,
            "embeds":self.embeds,
            "pinned":self.pinned,
            "mentions":self.mentions,
            "mention_roles":self.mention_roles,
            "attachments":self.attachments,
            "mention_everyone":self.mention_everyone,
            "tts":self.tts,
            "timestamp":self.timestamp,
            "edited_timestamp":self.edited_timestamp,
            "flags":self.flags,
            "components":self.components,
            "author":self.author.to_dict()
        }
        return Obj