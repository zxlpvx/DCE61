import discord
from discord.ext import commands
import json

with open('config.json') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'], self_bot=True)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='help')
async def help(ctx):
    await ctx.send('Help command')

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned')

@bot.command(name='unban')
async def unban(ctx, member: discord.Member):
    await member.unban()
    await ctx.send(f'{member} has been unbanned')

@bot.command(name='removefriends')
async def removefriends(ctx):
    for friend in bot.user.friends:
        await friend.remove_friend()
        print(f'Removed friend {friend}')
    await ctx.send('Removed all friends')

@bot.command(name='leaveservers')
async def leaveservers(ctx):
    for guild in bot.guilds:
        await guild.leave()
        print(f'Left server {guild}')
    await ctx.send('Left all servers')

@bot.command(name='closedms')
async def closedms(ctx):
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            await channel.close()
            print(f'Closed DM {channel}')
    await ctx.send('Closed all DMs')

@bot.command(name='makeservers')
async def makeservers(ctx, amount: int):
    for i in range(amount):
        guild = await bot.create_guild(f'Server {i+1}')
        print(f'Created server {guild}')
    await ctx.send('Created servers')

@bot.command(name='tokenlogin')
async def tokenlogin(ctx, token: str):
    try:
        bot.login(token)
        print('Logged in with token')
        await ctx.send('Logged in with token')
    except Exception as e:
        print(e)
        await ctx.send(str(e))

with open('token.txt', 'r') as f:
    token = f.read()

if __name__ == '__main__':
  try:
      bot.run(token, bot=False)
  except Exception as e:
      print(str(e))
