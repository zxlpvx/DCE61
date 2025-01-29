import discord

def get_member(guild, member_id):
  return guild.get_member(member_id)

def get_channel(guild, channel_id):
  return guild.get_channel(channel_id)
