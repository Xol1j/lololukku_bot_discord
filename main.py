import discord
from discord.ext import commands
import time
import os
import requests
import json
import random




bot_developers = [1113132313002397827,682217621898526783]

token='TOKEN'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
with open('Money.json', 'r') as j:
     userdata  = json.loads(j.read())

bot = commands.Bot(command_prefix=".",intents=intents)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def save_userdata():
    savef = open("Money.json","w+")
    savef.write(json.dumps(userdata))
    savef.close()

@bot.listen('on_ready')
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.listen('on_message')
async def on_message(message):
    prefc = False
    try:
        userdata["users"][str(message.author.id)]["balance"] = userdata["users"][str(message.author.id)]["balance"]
        prefc = True
    except:
        userdata["users"][str(message.author.id)] = {"balance":0}
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! <@{ctx.author.id}>')
@bot.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)
@bot.command()
async def dice(ctx,d1="6"):
    continueFlow = True
    try:
        d1 = int(d1)
    except:
        await ctx.send('```this is not a number \n please enter a number```')
        continueFlow = False
    if continueFlow:
        if(d1>1):
            await ctx.send('```'+str(random.randint(1,d1))+'🎲'+'```')
        else:
            await ctx.send("```mimimum number of the sides is 1```")
    
       # await ctx.send('```'+str(random.randint(1,d1))+'🎲'+'```')
@bot.command()
async def slot(ctx):
    if(userdata["users"][str(ctx.message.author.id)]["balance"]>=10):
        userdata["users"][str(ctx.message.author.id)]["balance"] -= 10
        el = ['🍊','🍋','🍌','🍒','7']
        er = []
        for i in range(3):
            er.append(random.choice(el))
        fws = "```"+er[0]+"|"+er[1]+"|"+er[2]+"```"
        if(er[0]==er[1] and er[1]==er[2]):
            fws += "\nCongratulations! It's a jackpot!"
            userdata["users"][str(ctx.message.author.id)]["balance"] += 50
        elif(er[0]==er[1] or er[1]==er[2]):
            fws += "\nCongratulations! You won!"
            userdata["users"][str(ctx.message.author.id)]["balance"] += 20
        else:
            fws += "\nMaybe you will be lucky next time!"
        await ctx.send(fws)
        save_userdata()
    else:
        await ctx.send("```You have no money. To play this game you should sell your soul to the devil!```")
@bot.command()
async def bal(ctx,d1='invalid syntax'):
    if d1 == 'invalid syntax':
        d1 = ctx.message.author.id
    try:
        await ctx.send(userdata['users'][str(d1)]["balance"])
    except:
        await ctx.send(0)
@bot.command()
async def eco(ctx,data1="error",data2="error",data3="error"):
    if(ctx.message.author.id in bot_developers):
        if(data1=="help" and data2=="error" and data3=="error"):
            await ctx.send("```.eco [set_money/give_money/take_money] <user ID> <money amount>```")
        elif(data1=="error" or data2=="error" or data3=="error"):
            await ctx.send("```diff\n-Invalid syntax!\nExample: .eco [set_money/give_money/take_money] <user ID> <money amount>```")
        else:
            if(data1=="set_money"):
                userdata["users"][data2] = {"balance":int(data3)}
            elif(data1=="give_money"):
                try:
                    userdata["users"][data2]["balance"]+=int(data3)
                except:
                    userdata["users"][data2] = {"balance":int(data3)}
            elif(data1=="take_money"):
                try:
                    userdata["users"][data2]["balance"]-=int(data3)
                except:
                    userdata["users"][data2] = {"balance":0-int(data3)}
            else:
                await ctx.send("```diff\n-Invalid syntax!\nExample: .eco [set_money/give_money/take_money] <user ID> <money amount>```""")
            uobj = await bot.fetch_user(int(data2))
            await ctx.send("```diff\n+Success! "+uobj.name+" now has "+str(userdata["users"][data2]["balance"])+" money```")
            save_userdata()
    else:
        await ctx.send("```diff\n-You do not have permissions to execute this command.```")
@bot.remove_command('help')
@bot.command()
async def help(ctx):
    await ctx.send("""
```
.bal - balance
.slot - slotmachine
.hello - greetings
.dice - dice roll
.quote - random quote generator
.bpg - bad password generator
.pg - password generator
.pin - random pin code generator
.ping - showing bots ping
```
""")
@bot.command()
async def info(ctx):
    await ctx.send("""
```
Bot is made by lololukku and  NikitaYarosh
Bot is currently in active development so if you found bug please contact the developers
discord: @petro_sosiska
```
""")
@bot.slash_command(name="init",guild_ids=[1232805929704099850])
async def slash_test(ctx):
    await ctx.respond("bot is running, type .help for help")

@bot.command()
async def bpg(ctx):
    
    lines = open('bfl03.txt').read().splitlines()
    myline =random.choice(lines)
    await ctx.send(myline)
@bot.command()
async def pin(ctx,digits="4"):
    from random import randint
    try:
        if(int(digits)<=10 and int(digits)>3):
            await ctx.send('```'+"".join([str(randint(0,9)) for i in range(int(digits))])+'```')
        else:
            await ctx.send("```Invalid amount of digits in pin, the maximum is 10, the minimum is 4.```")
    except:
        await ctx.send("```Invalid parameter```")

@bot.command()
async def pg(ctx,help=False):
    d = random.randint(1,9)
    d1 = random.randint(1,9)
    d = str(d)
    d1 = str(d1)
    sl = ('!','@','#','$','%','^','&','*','(',')')
    ss = random.choice(sl)
    ss1 = random.choice(sl)
    ll = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lc1 = random.choice(ll)
    lc = random.choice(ll)
    ul = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    uc = random.choice(ul)
    ps = d+ss+d1+lc+lc1+uc+ss1
    await ctx.send(ps)

@bot.command()
async def send(ctx,channel_id,d2):
    try:
        if ctx.message.author.id in bot_developers:
            channel = await bot.fetch_channel(channel_id)
            await channel.send(d2)
        else:
            await ctx.send("```you do not have a permission to use this command!```")
    except:
        await ctx.send("Invalid CID.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')
@bot.command()
async def admin_help(ctx):
    if ctx.message.author.id in bot_developers:
        await ctx.send('''
```
.eco [set_money,take_money,give_money] [uid] [amount] - economy
.send [cid] ["msg"] - send a message from bots name
.admin_help - administator commands help
.ar [cid] [mid] [reaction] - add reaction
.del_msg [cid] [mid] - delete message
```''')
    else:
        await ctx.send('```you do not have a permission to acsses this command!```')
@bot.command()
async def ar(ctx,channel_id,message_id,d1):
    if ctx.message.author.id in bot_developers:
        channel = await bot.fetch_channel(channel_id)
        message = await channel.fetch_message(message_id)
        await message.add_reaction(d1)
@bot.command()
async def burpfire(ctx,channel_id,message_id):
    if ctx.message.author.id in bot_developers:
        channel = await bot.fetch_channel(channel_id)
        message = await channel.fetch_message(message_id)
        await message.add_reaction("🗣")
        await message.add_reaction("🔥")
@bot.command()
async def del_msg(ctx,channel_id,message_id):
    if ctx.author.id in bot_developers:
        try:
            channel = await bot.fetch_channel(channel_id)
            message = await channel.fetch_message(message_id)
            await message.delete()
        except:
            await ctx.send('incorrect syntax')
    else:
        await ctx.send('you do not have permission to use this command')
bot.run(token)
