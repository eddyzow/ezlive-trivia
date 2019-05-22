from __future__ import division
import discord
client = discord.Client()
@client.event
async def on_message(message):
    global list
    global uniques
    global counts
    global percents
    if message.content.startswith('!RTB '):
        param, numbers = message.content.split('!RTB ')
        access = 0
        roles = []
        serverr = client.get_server('523339797104820273')
        roles.append(discord.utils.get(serverr.roles, name='Ruby Patron'))
        roles.append(discord.utils.get(serverr.server.roles, name='Sapphire Patron'))
        roles.append(discord.utils.get(serverr.server.roles, id='569974440620851201'))
        roles.append(discord.utils.get(serverr.server.roles, name='OG Donator'))
        for i in message.author.roles:
            if i in roles:
                access = 1
        if access == 1:
            lists = []
            numbers = list(str(numbers))
            lists = numbers
            stop = 'stop'
            uniques = []
            percents = []
            lists.sort()
            for i in range(0, len(lists)):
                if lists[i] not in uniques:
                    uniques.append(lists[i])
            uniques.sort()
            counts = []
            for i in range(0, len(uniques)):
                counts.append(lists.count(uniques[i]))
            for i in range(0, len(counts)):
                percents.append((counts[i]/sum(counts))*100)
            msg = ''
            for i in range(0, len(percents)):
                msg = msg+'Answer '+str(i+1)+': '+str(percents[i])+'%. \n'
            await client.send_message(message.channel, msg)
        else:
            await client.send_message(message.channel, 'To use this bot, become a patron at https://patreon.com/triviagameslive for $3/month or higher!')
        await client.delete_message(message)
    if message.content.startswith('!codebreak '):
        access = 0
        roles = []
        roles.append(discord.utils.get(message.author.server.roles, name='Ruby Patron'))
        roles.append(discord.utils.get(message.author.server.roles, name='Sapphire Patron'))
        roles.append(discord.utils.get(message.author.server.roles, id='569974440620851201'))
        roles.append(discord.utils.get(message.author.server.roles, name='OG Donator'))
        for i in message.author.roles:
            if i in roles:
                access = 1
        if access == 1:
            param, codebreak = message.content.split('!codebreak ',1)
            letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            if len(codebreak) <= 20:
                x = ''
                for i in range(0, len(codebreak)):
                    if codebreak[i] == ' ':
                        x = x +' '
                    else:
                        x = x+letters[letters.index(codebreak[i].lower())-1]
                await client.send_message(message.channel, x)
        else:
            await client.send_message(message.channel, 'To use this bot, become a patron at https://patreon.com/triviagameslive for $3/month or higher!')
        await client.delete_message(message)
async def on_ready():
    print(discord.__version__)
    print('Bot logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('NTc2ODE4NDE2NzkxNDUzNzE5.XNcCog.lN7claLzAfLFmu0YJ0fcZe3xINM')
    
    

                
                


                
                

