import discord 

from	discord.ext import commands 

class Events(commands.Cog):

	def __init__(self	,bot ):	self.bot			=	bot 


	async	def on_ready(self ):	print("Online ")
  

	def setup(bot ):	bot .add_cog(Events(bot ))
