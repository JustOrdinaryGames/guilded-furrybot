import os, time, json, random, guilded

expressions = ["OwO","owo","UwU","uwu","xd","x3",";3"]

os.system("@echo off")
os.system("cls")
os.system("title Guilded Furrybot")

try:
    config = json.load(open('config.json'))
    email = config.get('Email')
    password = config.get('Password')
except Exception as e:
    print('Cannot load the config, error: {e}')
    time.sleep(10)
    exit(0)

client = guilded.UserbotClient()

@client.event
async def on_ready():
    print('Logged into ' + client.user.name)

@client.event
async def on_message(message):
    if message.author != client.user:
        return
    if message.content == None:
        return
    msg = message.content
    msg = msg.replace("l", "w").replace("L", "W").replace("r", "w").replace("R", "W").replace("o", "u").replace("O", "U")
    msg = msg + " " + random.choices(expressions)[0]
    print('Old: "' + message.content + '" New: "' + msg + '"')
    await message.edit(content=msg)

print('Logging in...')
client.run(email,password)