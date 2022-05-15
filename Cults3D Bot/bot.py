import imp
import discord
from discord.ext import commands
from scrapper import scrapping

bot = commands.Bot(command_prefix='/', description="This is a scrapper bot")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Cults3D", url="http://www.twitch.tv/cults3D"))
    print('Bot ready')

async def format(message):
    await message.delete()
    data = scrapping(message.content)
    embed = discord.Embed(color=0x9955f7)
    embed.title = data["name"]
    embed.set_image(url=data["image_url"])
    embed.add_field(name="Prix", value=data["price"], inline=True)
    embed.add_field(name="Téléchargements", value=data["download"], inline=True)
    embed.add_field(name="URL", value=f"[Lien]({data['url']})", inline=True)
    await message.channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content.startswith("https://cults3d.com/") :
        await format(message)
    elif message.content.startswith("/format") :
        messages = await message.channel.history(limit=None).flatten()
        for message in messages[::-1]:
            if message.content.startswith("https://cults3d.com/"): 
                try:
                    await format(message)
                except:
                    pass
with open("token.txt", "r") as f:
    token = f.read()
bot.run(token)
