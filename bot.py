from discord.ext import commands
import discord
from datetime import datetime
import asyncio
import os
TOKEN = ""  # Dein Token

bot = commands.Bot(command_prefix="ocean!")  # Dein Prefix




#@bot.event
#async def on_ready():
    #channel = bot.get_channel(707219132701081680) # Deine Channel ID wo die Statistik gesendet werden soll
    #embed = discord.Embed(title='Server-Stats', color=discord.Color.green(), timestamp=datetime.utcnow())
    #embed.add_field(name='Mitglieder', value='?')
    #embed.add_field(name='Online', value='?')
    #embed.set_footer(text='Zuletzt aktualisiert:')
    #await channel.send(embed=embed)  # Wenn die Statistik gesendet wurde dieses Event löschen!



@bot.event
async def on_ready():
    bot.loop.create_task(stats_task())
    bot.loop.create_task(status_task2())


async def stats_task():
    while True:
        channel = bot.get_channel(707219132701081680)  # Deine Channel ID wo die 1. Message von der Statistik gesendet wurde
        message = await channel.fetch_message(707224166629113956)  # Die Message ID von der Gesendeten Statistik

        embed = discord.Embed(title='Server-Stats', color=discord.Color.green(), timestamp=datetime.utcnow(), description='Hier hast du eine kleine Übersicht über uns.')
        embed.add_field(name='Mitglieder', value=channel.guild.member_count, inline=True)
        embed.add_field(name='Online', value=len({m.id for m in channel.guild.members if m.status is not discord.Status.offline}), inline=True)
        #embed.add_field(name=' ⠀⠀',value= ' ⠀⠀', inline=False)
        #embed.add_field(name='Team Mitglieder:', value='Noch nicht festgelegt', inline=True)
        #embed.add_field(name='VIP Mitglieder:', value='Noch nicht festgelegt', inline=True)
        #embed.set_footer(text='Zuletzt aktualisiert:')
        await message.edit(embed=embed)
        await asyncio.sleep(600)  # = 10 Minuten

async def status_task2():
    colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(),
              discord.Colour.blue(), discord.Colour.purple()]
    while True:
        await client.change_presence(activity=discord.Game('Ersteller Canned Heat'), status=discord.Status.online)
        await asyncio.sleep(5)
        # await client.change_presence(activity=discord.Game('Mein cooler Bot!'), status=discord.Status.online)
        # await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('Aktualisiert die Stats'), status=discord.Status.online)
        await asyncio.sleep(5)

#bot.run(TOKEN)
client.run(os.getenv('Token'))
