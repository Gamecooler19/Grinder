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
async def help(ctx, colour, title, description, *,url):
  embed = discord.Embed(title="Gamecooler19's Grinder Self Bot", type='rich', color=420699, description=f"**{prefix}owostart**\n Sends A OwO Trick Made By Gamecooler19 In Every 50 seconds.\n\n**{prefix}owostop**\n Stops Auto OwO. \n\n\n\n**{prefix}dmcstart**\n Sends A Dank Memer Trick Made By Gamecooler19 In Every 50 seconds.\n\n**{prefix}dmcstop**\n Stops Auto Dank Memer.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/917333971061329930/a_dd370765088466ccd900412d75eb29d9.gif?size=1024")
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def owostart(ctx):
	await ctx.message.delete()
	await ctx.send('Auto OwO Is Now **enabled**!')
	global owocs
	owocs = True
	while owocs:
		async with ctx.typing():
			 await asyncio.sleep(17)
			 await ctx.send('owo pray <@758697679667855433>')
			 print(f"{Fore.GREEN}succefully prayed")
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
async def owostop(ctx):
	await ctx.message.delete()
	await ctx.send('Auto OwO Is Now **Disabled**!')
	global owocs
	owocs = False


@client.command(pass_context=True)
async def dmcstart(ctx):
	await ctx.message.delete()
	await ctx.send('Auto Dank Memer Is Now **Enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}succesfully begged")
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succesfully fished") 
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succesfully hunt")
			await ctx.send('pls dep all')
			print(f"{Fore.GREEN}succesfully deposited all")
			await asyncio.sleep(47)
			
@client.command()
async def dmcstop(ctx):
	await ctx.message.delete()
	await ctx.send('Auto Dank Memer Is Now **Disabled**!')
	global owocs
	owocs = False

@client.event
async def on_ready():
  activity = discord.ActivityType.watching(name="Gamecooler19 On Youtube")
  await client.change_presence(status=discord.Status.dnd, activity=activity)
  print(f'''{Fore.RED} 
 
  _____                                      _          __  ___  
 / ____|                                    | |        /_ |/ _ \ 
| |  __  __ _ _ __ ___   ___  ___ ___   ___ | | ___ _ __| | (_) |
| | |_ |/ _` | '_ ` _ \ / _ \/ __/ _ \ / _ \| |/ _ \ '__| |\__, |
| |__| | (_| | | | | | |  __/ (_| (_) | (_) | |  __/ |  | |  / / 
 \_____|\__,_|_| |_| |_|\___|\___\___/ \___/|_|\___|_|  |_| /_/  
                                                                 
                                                                 
{Fore.RED}
  

{Fore.GREEN}


  _____      _           _           
 / ____|    (_)         | |          
| |  __ _ __ _ _ __   __| | ___ _ __ 
| | |_ | '__| | '_ \ / _` |/ _ \ '__|
| |__| | |  | | | | | (_| |  __/ |   
 \_____|_|  |_|_| |_|\__,_|\___|_|   
                                     
                                     

selfbot is ready!
''')

client.run(token, bot=False)

