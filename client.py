# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents = intents)
#
# #On ready event
# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break
#     print(f'{client.user} has connected to Discord!')
#     print(f'Currently connected to: {guild.name}(id: {guild.id})')
#
# #On member join event
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#                 f'Hi {member.name}'
#             )
# #On new message event
# @client.event
# async def on_message(message):
#     # Checks if the message was sent by itself 
#     if message.author == client.user:
#         return
#     #Test 
#     if message.content == 'Ping me':
#         await message.channel.send("Pong me")
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
#
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise
#
# client.run(TOKEN)
