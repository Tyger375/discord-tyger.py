class User():
    def __init__(self, username, id, discriminator, avatar, public_flags, bot):
        self.username = username
        self.id = id
        self.discriminator = discriminator
        self.avatar = avatar
        self.public_flags = public_flags
        self.bot = bot

    def to_dict(self):
        user = {
            "username":self.username,
            "id":self.id,
            "discriminator":self.discriminator,
            "avatar":self.avatar,
            "public_flags":self.public_flags,
            "bot":self.bot,
        }
        return str(user)