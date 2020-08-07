import discord
import random
from chars import chars
from settings import settings

client = discord.Client()
lastNum = 0


@client.event
async def on_ready():
    print('ready')
    print(len(chars['kokichi']['images']))


@client.event
async def on_message(message: discord.Message):
    global lastNum
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
        rand = random.randint(0, len(char['images'])-1)

        while lastNum == rand:
            rand = random.randint(0, len(char['images'])-1)

        lastNum = rand
        print(rand)
        embed.set_image(url=char['images'][rand])
        await message.channel.send(embed=embed)


client.run(settings['token'])
