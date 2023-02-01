import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

BOT_TOKEN = "something something"
CHANNEL_ID = 1070022425724600411

client = commands.Bot(command_prefix="-", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Connection successful with Discord")
    channel = client.get_channel(CHANNEL_ID)  # get the channel in into the variable
    await channel.send(
        "Booted Up Successfully"
    )  # await is used to wait for this command to finish

    change_status.start()  # start the change status loop


# greetings
@client.command()
async def hello(ctx):
    await ctx.send("Hello!")


# addition
@client.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result = result + int(i)
    await ctx.send(result)


# converter
@client.command()
async def dec2bin(ctx, x):
    result = bin(int(x)).replace("0b", "")
    await ctx.send(result)


@client.command()
async def dec2hex(ctx, x):
    result = hex(int(x)).replace("0x", "")
    cap = str(result)
    await ctx.send(cap.capitalize())


@client.command()
async def dec2oct(ctx, x):
    result = oct(int(x)).replace("0o", "")
    await ctx.send(result)


# Magic8ball
@client.command(aliases=["nani", "bhay"])
async def magic(ctx, *, question):
    with open("answers.txt", "r") as f:  # input the anwsers file
        all_responses = f.readlines()  # read the lines in the file
        random_response = random.choice(
            all_responses
        )  # chooses a random line from the file
    await ctx.send(random_response)

# russian_roulette
@client.command(aliases=["gun", "spinit", "spin it"])
async def spin(ctx):
    with open("magazine.txt", "r") as f:
        all_responses = f.readlines()
        random_response = random.choice(
            all_responses
        )
    await ctx.send(random_response)

# latency
@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"Bot's Latency: {bot_latency}ms.")


bot_status = cycle(["Hi!!", "Hello!!", "Namaste!!", "Namaskar!!", "Konnichiwa!!", "Hola!!", "Bonjour!!", "Guten tag!!"])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


client.run(BOT_TOKEN)  # looping function
