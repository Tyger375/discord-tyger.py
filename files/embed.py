

class Embed():
    def __init__(self, title="undefined", description="undefined", color=0):
        self.title = title
        self.description = description
        self.color = color
        self.fields = []
        self.footer = {}
        self.thumbnail = {}
        self.image = {}
        self.author = {}

    def to_dict(self):
        embed = {}
        embed["title"] = self.title
        embed["description"] = self.description
        embed["color"] = self.color
        embed["fields"] = self.fields
        embed["footer"] = self.footer
        embed["thumbnail"] = self.thumbnail
        embed["image"] = self.image
        embed["author"] = self.author
        return embed

    def add_field(self, value="undefined", name="undefined", inline=False):
        Field = {}
        Field["name"] = name
        Field["value"] = value
        Field["inline"] = inline
        self.fields.append(Field)

    def set_footer(self, text="undefined", icon_url="undefined"):
        footer = {}
        footer["text"] = text
        if icon_url != "undefined":
            footer["icon_url"] = icon_url
        self.footer = footer

    def set_thumbnail(self, url):
        thumbnail = {
            "url":url
        }
        self.thumbnail = thumbnail

    def set_image(self, url):
        image = {
            "url":url
        }
        self.image = image

    def set_author(self, name, url=None, icon_url=None):
        author = {}
        author["name"] = name
        if url != None:
            author["url"] = url
        if icon_url != None:
            author["icon_url"] = icon_url
        self.author = author