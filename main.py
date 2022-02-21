import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "$$"

#use the .env feature to hide your token

keep_alive()
token = os.environ('TOKEN')
#---------------#

client = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@client.command()
async def help(ctx):
  embed = discord.Embed(title="Gamecooler19's Auto OwO", color=420699, description=f"**{prefix}start**\n Sends A Trick Made By Gamecooler19 In Every 50 seconds.\n\n**{prefix}stop**\n Stops Auto OwO.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/912767456081235999/a_50d94ee7e9b7a2ccefd649bafbcb1a33.gif?size=1024")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def start(ctx):
	await ctx.message.delete()
	await ctx.send('Auto OwO is now **enabled**!')
	global owocs
	owocs = True
	while owocs:
		async with ctx.typing():
			 await asyncio.sleep(47)
			 await ctx.send('owo flip 1')
			 print(f"{Fore.GREEN}succefully fliped")
			 await asyncio.sleep(17)
			 await ctx.send('owo flip 1')
			 print(f"{Fore.GREEN}succefully fliped")
			 await asyncio.sleep(17)
			 await ctx.send('owo flip 1')
			 print(f"{Fore.GREEN}succefully fliped")
			 await asyncio.sleep(17)
			 await ctx.send('owo flip 50000')
			 print(f"{Fore.GREEN}succefully fliped")
			 await asyncio.sleep(17)
			 await ctx.send('owo cash')
			 print(f"{Fore.GREEN}succefully balanced")
       



@client.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('Auto OwO Is Now **Disabled**!')
	global owocs
	owocs = False

@client.event
async def on_ready():
  activity = discord.Game(name="Minecraft", type=4)
  await client.change_presence(status=discord.Status.dnd, activity=activity)
  print(f'''{Fore.RED}
                                                                        ▄▄                                
  ▄▄█▀▀▀█▄█                                                           ▀███                                
▄██▀     ▀█                                                             ██                  ▄▄▄           
██▀       ▀ ▄█▀██▄ ▀████████▄█████▄   ▄▄█▀██ ▄██▀██  ▄██▀██▄  ▄██▀██▄   ██   ▄▄█▀██▀███▄███▀███   ▄█▄▀▄█▄▄
██         ██   ██   ██    ██    ██  ▄█▀   ███▀  ██ ██▀   ▀████▀   ▀██  ██  ▄█▀   ██ ██▀ ▀▀  ██  ███    ██
██▄    ▀████▄█████   ██    ██    ██  ██▀▀▀▀▀▀█      ██     ████     ██  ██  ██▀▀▀▀▀▀ ██      ██  ███    ██
▀██▄     ████   ██   ██    ██    ██  ██▄    ▄█▄    ▄██▄   ▄████▄   ▄██  ██  ██▄    ▄ ██      ██   ▀███████
  ▀▀███████▀████▀██▄████  ████  ████▄ ▀█████▀█████▀  ▀█████▀  ▀█████▀ ▄████▄ ▀█████▀████▄  ▄████▄      ▄█▀
                                                                                                    ▄██   
                                                                                                  █▀▀     

{Fore.RED}
  

{Fore.GREEN}
                                                                                   
      ██                  ██                 ▄▄█▀▀██▄                    ▄▄█▀▀██▄  
     ▄██▄                 ██               ▄██▀    ▀██▄                ▄██▀    ▀██▄
    ▄█▀██▄   ▀███  ▀███ ██████  ▄██▀██▄    ██▀      ▀████▀    ▄█    ▀██▀█▀      ▀██
   ▄█  ▀██     ██    ██   ██   ██▀   ▀██   ██        ██ ██   ▄███   ▄█ ██        ██
   ████████    ██    ██   ██   ██     ██   ██▄      ▄██  ██ ▄█  ██ ▄█  ██▄      ▄██
  █▀      ██   ██    ██   ██   ██▄   ▄██   ▀██▄    ▄██▀   ███    ███   ▀██▄    ▄██▀
▄███▄   ▄████▄ ▀████▀███▄ ▀████ ▀█████▀      ▀▀████▀▀      █      █      ▀▀████▀▀  
                                                                                   
                                                                                   

selfbot is ready!
''')

client.run(token, bot=False)

