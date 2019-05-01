#GeoBot v0.1.0 rewrite version.
#https://github.com/Fellox/Geobot
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='g!')
TOKEN = 'NTQ4MjgzOTU1MDc0MzAxOTcy.XMjQhg._scWw4Rxz2TvKLwfk7_1bMEUfqg'

@bot.event
def on_ready():
    await bot.remove_command('help')
    channel = bot.get_channel(547600921035669516)
    print('Corriendo!')
    await bot.channel.send(channel, '¡Listo para rodar!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(bot.latency * 1000)}ms`')

@bot.command()
async def masterhelp():
    embed = discord.Embed(title='Lista de Comandos', description='Lista de Comandos para GeoBot', colour=discord.Colour.blue)
    embed.set_footer(text='Hecho por [Fellox]')
    embed.add_field(name='g!ping', value='Devuelve un comando con `Pong!` y la latencia del bot.')
    await bot.say(embed=embed)

@bot.command()
async def fellox():
    await bot.say('A su ordenes!')
bot.run(TOKEN)
