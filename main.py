import discord
import random
from chars import chars
from settings import settings

client = discord.Client()


@client.event
async def on_ready():
    print('ready')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content == '$$help':
        await message.channel.send(embed=discord.Embed(
            color=0xC934FF,
            description=u'список пидорасов: \n' + ('\n'.join(map(lambda k: "$$" + k, chars.keys())))
        ))
    elif message.content.startswith('$$'):
        char = chars[message.content[2:]]
        embed = discord.Embed(color=char['color'])
        embed.title = char['title']
        embed.set_image(url=random.choice(char['images']))
        await message.channel.send(embed=embed)


client.run(settings['token'])
