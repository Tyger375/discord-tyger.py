import asyncio
import files.poggers as discord

client = discord.Client("token")

async def on_message(message):
    if message.author.bot == False:
        #print(message)
        #print(message.id, message.author.username, message.channel.id)
        Embed = discord.Embed(title="lol", description="poggers", color=discord.EmbedColor.yellow())
        Embed.add_field(name="ciao", value=message.author.username)
        if message.content == "!pog":
            #await message.delete()
            messaggio = await message.channel.send("ciao", embeds=[Embed])
            await asyncio.sleep(2)
            #poggers = await messaggio.edit("poggers")
            #print(poggers.content)
        if message.content == "!test":
            await message.channel.send(f"ciao {message.author.username}!")

while True:
    message = client.getMessage()
    if message != None:
        asyncio.run(on_message(message))
