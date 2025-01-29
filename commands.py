import discord
from discord.ext import commands

class Commands(commands.Cog):

  def __init__(self, bot):
      self.bot = bot

  @commands.command(name="mute")
  async def mute(self,ctx ,member :discord.Member) :
      role =discord.utils.get(member.guild.roles ,name ="Muted")
      if not role :
          role=await member.guild.create_role( name="Muted")
          for channels in member.guild.text_channels :
              perms=channels.overwrites_for(role )
              perms.read_messages=False 
              perms.read_message_history=False 
              perms.add_reactions=False 
              perms.attach_files= False 
              perms.embed_links=False 
              perms.speak= False  
              perms.use_slash_commands= False  
              channels.set_permissions(role , overwrite=perms )      
          embedVar2 =discord.Embed(title=f"Member Muted" , description=f"You Have Been Muted By **{ctx.author.name}**) " ,color=(0Xff0000))       
          embedVar2.add_field( name=f"Reason:" ,value="No reason provided", inline=True)          
          embedVar2.set_footer(text="Try Not To Get muted Again")        
          embedVar2.timestamp()   
          try :
            return    	await member.create_dm().send(embed=(embedVar2))    
          except :   
             pass                
      else :        
         try :
           embedVar3 =discord.Embed(title=f"Member Unmuted " , description=f"You Have Been unmuted by **{ctx.author.name}) ")     
           embedVar3.set_footer(text="Try Not To Get muted Again")        
           embedVar3.timestamp()   
           return		await member.create_dm().send(embed=(embedVar3))    
         except :   
             pass       
      if not role in member.roles :
      	 	try :
      	 		embedVardm4=discord.Embed(title=f"Mute Warning!" , description=(f"{member.mention} You have been warned!"))
      	 		embedVardm4.timestamp()  
      	 		await	ctx.respond((f"{member.mention} You have been warned!"))	
      	 		return	await	member.create_dm().send(embed=((embedVardm4)))
      		except Exception	as e :	
      			print(e)	
      			pass          
      	 	if not role	in(member.roles):		
      		try :			
      			await	member.add_roles(role )			
      		except Exception	as e		:
      			print(e)		
      			pass           
      	else :		
      		return	discord.utils.get(member .guild .roles,name ="UnMute")	

def setup(bot):      
	bot.add_cog(Commands(bot))
