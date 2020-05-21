#-->******************* | Imports | ******************<--#
import re, sqlite3, discord, random
from os.path import isfile
import asyncio
class matches:
    def __init__(self, bot_match_id, capA, capB):
        self.bot_match_id = bot_match_id
        self.CapA = capA
        self.CapB = capB
a = []
bot_id = 0
teams_rdy = 0
channel_id = 0
#database()
cancel_match = 0
sub_message = 0
last_map = -1
last_last_map = -1
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    global bot_id
    global a
    global cancel_match
    global sub_message
    global last_map
    global last_last_map
    global teams_rdy
    if 'pickup has been started!' in message.content and (message.author.bot == True or message.author.id == 219601900486656000): 
        mes = ""
        mda1 = ""
        mda2 = ""
        mmm = ""

        if last_last_map == "Abbey" or last_map == "Abbey":
            mda1 = mda1 +"```ml\n📛- Abbey```"
        else:
            mda1 = mda1 +'```prolog\n0️ Abbey```'
        if last_last_map == "Austria" or last_map == "Austria":
            mda1 = mda1 +"```ml\n📛- Austria```"
        else:
            mda1 = mda1 +'```prolog\n1️ Austria```'
        if last_last_map == "Casa" or last_map == "Casa":
            mda1 = mda1 +"```ml\n📛- Casa```"
        else:
            mda1 = mda1 +'```prolog\n2️ Casa```'
        if last_last_map == "Kingdom" or last_map == "Kingdom":
            mda1 = mda1 +"```ml\n📛- Kingdom```"
        else:
            mda1 = mda1 +'```prolog\n3️ Kingdom```'
        if last_last_map == "Orbital_sl" or last_map == "Orbital_sl":
            mda1 = mda1 +"```ml\n📛- Orbital_sl```"
        else:
            mda1 = mda1 +'```prolog\n4️ Orbital_sl```'
        if last_last_map == "Prague" or last_map == "Prague":
            mda2 = mda2 +"```ml\n📛- Prague```"
        else:
            mda2 = mda2 +'```prolog\n5️ Prague```'
        if last_last_map == "Sanctuary" or last_map == "Sanctuary":
            mda2 = mda2 +"```ml\n📛- Sanctuary```"
        else:
            mda2 = mda2 +'```prolog\n6️ Sanctuary```'
        if last_last_map == "Tohunga_b8" or last_map == "Tohunga_b8":
            mda2 = mda2 +"```ml\n📛- Tohunga_b8```"
        else:
            mda2 = mda2 +'```prolog\n7️ Tohunga_b8```'
        if last_last_map == "Turnpike" or last_map == "Turnpike":
            mda2 = mda2 +"```ml\n📛- Turnpike```"
        else:
            mda2 = mda2 +'```prolog\n8️ Turnpike```'
        if last_last_map == "Uptown" or last_map == "Uptown":
            mda2 = mda2 +"```ml\n📛- Uptown```"
        else:
            mda2 = mda2 +'```prolog\n9️ Uptown```'

        embed = discord.Embed(colour=discord.Colour(0x50e3c2), description="{0}".format(mmm))

        embed.add_field(name="**MAP LIST 1**", value="{0}".format(mda1), inline=True)
        embed.add_field(name="**MAP LIST 2**", value="{0}".format(mda2), inline=True)

        m = embed
        await asyncio.sleep(1)
        await message.channel.send(content=mes+"**Vote for a map**:",embed = m)
        await message.channel.send("```md\n#Timer started! ---> |1️⃣5️⃣ Seconds left\n```")
    if 'Timer started!' in message.content and (message.author.bot == True or message.author.id == 219601900486656000): 
        if message.author.id == 219601900486656000:
            await message.channel.send(message.content)
            await message.delete()
            return
        seconds = 3
        mm = message.content
        and_sec = 0
        timer = 0
        while timer >= 0:
            and_sec -= 2
            if and_sec <= -1:
                seconds -= 1
                and_sec = 9
            await asyncio.sleep(2)
            mm = "```md\n#Timer started! ---> |"+numbers(seconds)+""+numbers(and_sec)+"| Seconds left\n```"

            timer -= 1
            await message.edit(content=str(mm))
        await message.delete()
        
            
            
        
    if 'Vote for a map**:' in message.content and (message.author.bot == True or message.author.id == 219601900486656000): 
        mentionss = message.mentions
        await message.edit(content=str("**Vote for a map**:"))
        maps = []
        emojis_check = []
        mm = "```\n"
        if last_map != "Abbey" and last_last_map != "Abbey":
            await message.add_reaction('0️⃣')
            maps.append("Abbey")
            emojis_check.append('0️⃣')
        if last_map != "Austria" and last_last_map != "Austria":
            await message.add_reaction('1️⃣')
            maps.append("Austria")
            emojis_check.append('1️⃣')
        if last_map != "Casa" and last_last_map != "Casa":
            await message.add_reaction('2️⃣')
            maps.append("Casa")
            emojis_check.append('2️⃣')
        if last_map != "Kingdom" and last_last_map != "Kingdom":
            await message.add_reaction('3️⃣')
            maps.append("Kingdom")
            emojis_check.append('3️⃣')
        if last_map != "Orbital_sl" and last_last_map != "Orbital_sl":
            await message.add_reaction('4️⃣')
            maps.append("Orbital_sl")
            emojis_check.append('4️⃣')
        if last_map != "Prague" and last_last_map != "Prague":
            await message.add_reaction('5️⃣')
            maps.append("Prague")
            emojis_check.append('5️⃣')
        if last_map != "Sanctuary" and last_last_map != "Sanctuary":
            await message.add_reaction('6️⃣')
            maps.append("Sanctuary")
            emojis_check.append('6️⃣')
        if last_map != "Tohunga_b8" and last_last_map != "Tohunga_b8":
            await message.add_reaction('7️⃣')
            maps.append("Tohunga_b8")
            emojis_check.append('7️⃣')
        if last_map != "Turnpike" and last_last_map != "Turnpike":
            await message.add_reaction('8️⃣')
            maps.append("Turnpike")
            emojis_check.append('8️⃣')
        if last_map != "Uptown" and last_last_map != "Uptown":
            await message.add_reaction('9️⃣')
            maps.append("Uptown")
            emojis_check.append('9️⃣')
        await asyncio.sleep(61*1) #####################################
        max = 0
        maxxx=[]
        count = 0
        last_max = 0
        kk=0
        mm = mm + "People,who can vote are: "
        for i in mentionss:
            mm=mm+""+i.display_name+", "
        mm = mm + "\n----------------------------------------------\n"
        for n in message.reactions:
            for o in emojis_check:
                if o == n.emoji:
                    users = await n.users().flatten()
                    new_count = 0
                    for user in users:
                        for i in mentionss:
                            if user.id==i.id:
                                new_count +=1
                                mm = mm + "|"+user.display_name+"| "
                    if new_count > last_max:
                        max = count
                        last_max = new_count
                    if new_count != 0:
                        kk+=1
                        mm = mm + "voted for: "+o+"\t"+ "In total: ["+str(new_count)+"] votes for "+o+" which is: **"+maps[count]+"**\n"
                    count+=1
        count = 0
        for n in message.reactions:
            for o in emojis_check:
                if o == n.emoji:
                    users = await n.users().flatten()
                    new_count = 0
                    for user in users:
                        for i in mentionss:
                            if user.id==i.id:
                                new_count +=1
                    if new_count == last_max:
                        maxxx.append(count)
                    count+=1
                                
        if len(maxxx)>1 or kk == 0:
            max = maxxx[random.randrange(-1, len(maxxx))]
        last_last_map = last_map
        last_map = maps[max]
        mm = mm + "\n Map: {0}\n```".format(maps[max])
        await message.guild.get_channel(580474846077648897).send(mm) ##change  ##
        await message.channel.send("Map: **{0}**".format(maps[max]))
        await message.delete()
               
def numbers(num):
    mmm = ""
    if num == 0:
        mmm = "0️⃣"
    elif num == 1:
        mmm = "1️⃣"
    elif num == 2:
        mmm = "2️⃣"
    elif num == 3:
        mmm = "3️⃣"
    elif num == 4:
        mmm = "4️⃣"
    elif num == 5:
        mmm = "5️⃣"
    elif num == 6:
        mmm = "6️⃣"
    elif num == 7:
        mmm = "7️⃣"
    elif num == 8:
        mmm = "8️⃣"
    elif num == 9:
        mmm = "9️⃣"
    return mmm
    

client.run('NzEyMzIzNzE5Njc4Mzk0NDI5.XsQh9w.P1_R2qB59GnPn1TTND5VUrCw-Vk')