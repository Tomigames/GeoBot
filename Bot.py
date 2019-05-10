#GeoBot v0.1.0 rewrite version.
#https://github.com/Fellox/Geobot
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='g!')
TOKEN = 'NTQ4MjgzOTU1MDc0MzAxOTcy.XMjQhg._scWw4Rxz2TvKLwfk7_1bMEUfqg'

@bot.event
async def on_ready():
    channel = bot.get_channel(547600921035669516)
    print('Corriendo!')
    await channel.send('¡Listo para rodar!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(bot.latency * 1000)}ms`')

@bot.command()
async def ayuda(ctx):
    await ctx.send('''
    ===============================
    **_Lista de Comandos_**

    `g!ping`
    Envia un mensaje con la latencia del bot.

    `g!ayuda`
    Envia este mensaje

    `g!randint`
    Genera un numero
    ===============================
    ''')

@bot.command()
async def shutdown(ctx):
    await ctx.send('Shuting down internal server.')
    exit()

@bot.command()
async def randint(ctx):
    number = random.randint(1, 10)
    await ctx.send('El numero elejido fue: `' + str(number) + '`')
bot.run(TOKEN)
