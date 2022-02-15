import os
import discord
#import asyncio
#import datetime
from discord.ext import commands
from keep_alive import keep_alive

# this is how to create the prefix of the bot
prefix = "./"
bot = commands.Bot(command_prefix = prefix)


# basically turns the bot on
@bot.event
async def on_ready():
    print("Everything's all ready to go~", bot.user)


# this is how commands are made
@bot.event
async def on_message(message):
  # we do not want the bot to reply to itself
  if message.author == bot.user:
    return

  # Whenever the bot is tagged, respond with its prefix
  if message.content.startswith(f'<@!{bot.user.id}>') and len(message.content) == len(f'<@!{bot.user.id}>'):
      await message.channel.send(f'My prefix here is `{prefix}`')

  # print to console the user and what they typed
  '''
  print(message.author)
  print('The message's content was:', message.content)
  '''
  # allows the bot to send messages from commands to discord
  await bot.process_commands(message)


# this is how all commands function. this command is the ping command
@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send('pong ' + str(latency))


# this is how a miniboss is started
@bot.command(name = 'start')
async def start(ctx):
  'This is the start command for the miniboss'

  await ctx.send('time for a mb! type `join` to join')

  join_count = 0
  i = []

  async def miniboss(i, join_count):
    mb_list = ' '.join(i)
    await ctx.send('`rpg miniboss ' + mb_list + '`')

    '''
    if join_count == 1:
      await ctx.send('`rpg miniboss ' + mb_list + '`')
    elif join_count == 2:
      await ctx.send('`rpg miniboss ' + mb_list + '`')
    elif join_count == 3:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + '`')
    elif join_count == 4:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3]+ '`')
    elif join_count == 5:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3] + i[4] + '`')
    elif join_count == 6:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + '`')
    elif join_count == 7:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + '`')
    elif join_count == 8:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + '`')
    elif join_count == 9:
      await ctx.send('`rpg miniboss ' + i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8] + '`')
    '''
  
  # check the join input
  def check(msg):
    return msg.channel == ctx.channel and \
    msg.content.lower() in ['join', 'stop']

  while join_count < 10:
    if join_count != 9:

      # it was here but works better to iteratte in the join flag
      #join_count += 1
      # check the join input from 'def check'
      msg = await bot.wait_for('message', check=check)
    
      if msg.content.lower() == 'join':
        mb_id = '<@' + str(msg.author.id) + '>'
        #i.append(str(msg.author.id))
        i.append(mb_id)
        # checks to be sure user input was correct (debug purposes)
        #await ctx.send('You said join!')
        join_count += 1
      elif msg.content.lower() == 'stop':
        await ctx.send('<@'+str(ctx.author.id)+'> You said stop!')
        # sends how many people typed join (debug purposes)
        #await ctx.send(join_count)
        # passes the array and join_count to boss for partially filled output
        await miniboss(i, join_count)
        # sends the full array for checks (debug purposes)
        #await ctx.send(i)
        break
    else:
      await miniboss(i, join_count)
      join_count += 1

    


# this is how an arena is started
@bot.command(name = 'startarena', aliases = ['starta', 'astart', 'arenastart'])
async def startarena(ctx):
  'Start the arena message'

  await ctx.send('The arena menu is starting')

  a = ['---', '---', '---', '---', '---', '---', '---', '---', '---', '---']
  join_count = 0
  
  async def arenamsg(ctx, a):
    nameslist = '\n'.join(a)

    embed=discord.Embed(title='Nazarick Boosted Arena', color=0xb51a00)
    #embed.set_author(url=ctx.author.display_name, icon_url=ctx.author.display_icon)
    embed.add_field(name='INSTRUCTIONS', value='blank', inline=False)
    embed.add_field(name='Arena', value=nameslist, inline=False)
    embed.set_footer(text='Nazarick Boosted Arena')
    await ctx.send(embed=embed)
  
  await arenamsg(ctx, a)

  def check(msg):
    return msg.channel == ctx.channel and \
    msg.content.lower() in ['a in', 'a out']

  while True:
    if join_count != 10:

      msg = await bot.wait_for('message', check=check)

      if msg.content.lower() == 'a in':
        arena_id = '<@' + str(msg.author.id) + '>'
         
        if arena_id in a:
          await ctx.send(arena_id + 'You are already in the list')
        else:
          a.remove(a[join_count])
          a.insert(join_count, arena_id)
          join_count += 1
        
        await arenamsg(ctx, a)

      elif msg.content.lower() == 'a out':
        '''
        replace first userid in a 
        '''

      

# delete previous message?
# await ctx. message. delete()


#keep_alive() # runs the webserver
bot.run(os.getenv('shush')) #just a trade secret
