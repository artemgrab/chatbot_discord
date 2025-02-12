import discord
from discord.ext import commands
import random
import os.path

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

emoji_ids = ["1157344917580947516", "1157345030172839997", "1157344305594257491", "1157344800585023598",
             "1157344500771991562", "1157343850948464811", "1157344411324256367", "1157344042116448388",
             "1157345253905412116", "1182024290250539089", "1157345253905412116", "1157345588522799164",
             "1169926622250545243", "1157344667638177852", "1194347453810495509", "1157343753653207060"]


@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Game(name="Roblox"))

    # with open("messages.txt", "a") as file:
    # file.write(f"{text.content}\n")


with open("messages.txt") as inp:
    lines = inp.readlines()
message_count = {}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.reference and message.reference.resolved.author == client.user:
        random_line3 = random.choice(lines).strip()
        await message.channel.send(random_line3)

    if 'Француз' in message.content or 'француз' in message.content:
        random_line = random.choice(lines).strip()
        await message.channel.send(random_line)

    if 'француз' not in message.content.lower():
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f"{message.content}\n")
        lines.append(message.content)

    chance = 0.1

    if random.random() < chance:
        emoji_id = random.choice(emoji_ids)
        emoji = await message.guild.fetch_emoji(emoji_id)
        await message.add_reaction(emoji)

    author_id = message.author.id
    message_count[author_id] = message_count.get(author_id, 0) + 1
    if message_count[author_id] % 30 == 0:
        random_line2 = random.choice(lines).strip()
        await message.channel.send(random_line2)


lines = []
if os.path.exists("messages.txt"):
    with open("messages.txt") as inp:
        lines = inp.readlines()

client.run(DISCORD_TOKEN)
