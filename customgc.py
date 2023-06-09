import discord
import json
import asyncio

client = discord.Client() 

block_word1 = 'discord.gg'
block_word2 = 'しね'
block_word3 = '死ね'
block_word4 = '@everyone'
block_word5 = '@here'
ban_list = {}

chat_name = "ズミン！グローバル！"

async def zumingc(message):
    with open('zumin-gloval/banlist.json', 'r') as file:
        banlist = json.load(file)
    
        user_id = message.author.id
    
        if user_id in banlist:
        #メッセージをブロック
         await message.add_reaction('<:error:1041554270958387220>')
         await message.delete()
         embed = discord.Embed(title="お知らせ",description="現在、あなたは利用制限を受けているため、グローバルチャットの利用ができません。",color=0xff0000) 
         await message.author.send(embed=embed)
         return
         #banユーザーをブロック
    if  message.content.find(block_word1) != -1:
        await message.author.send('Discordサーバーの宣伝行為はは許可されていません！')
        await message.add_reaction('<:error:1041554270958387220>')
        channel = client.get_channel(1067177909657288804)
        embed = discord.Embed(description=message.content,color=0xff0000) 
        embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id,message.author.avatar))
        embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
        await channel.send(embed=embed)
        await message.delete()
        return
    if  message.content.find(block_word2) != -1:
        await message.author.send('ブロックされた単語の送信は許可されていません！')
        await message.add_reaction('<:error:1041554270958387220>')
        channel = client.get_channel(1067177909657288804)
        embed = discord.Embed(description=message.content,color=0xff0000) 
        embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id,message.author.avatar))
        embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
        await channel.send(embed=embed)
        await message.delete()
        return
    if  message.content.find(block_word3) != -1:
        await message.author.send('ブロックされた単語の送信は許可されていません！')
        await message.add_reaction('<:error:1041554270958387220>')
        channel = client.get_channel(1067177909657288804)
        embed = discord.Embed(description=message.content,color=0xff0000) 
        embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id,message.author.avatar))
        embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
        await channel.send(embed=embed)
        await message.delete()
        return
    if  message.content.find(block_word4) != -1:
        await message.author.send('ブロックされた単語の送信は許可されていません！')
        await message.add_reaction('<:error:1041554270958387220>')
        channel = client.get_channel(1067177909657288804)
        embed = discord.Embed(description=message.content,color=0xff0000) 
        embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id,message.author.avatar))
        embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
        await channel.send(embed=embed)
        await message.delete()
        return
    if  message.content.find(block_word5) != -1:
        await message.author.send('ブロックされた単語の送信は許可されていません！')
        await message.add_reaction('<:error:1041554270958387220>')
        channel = client.get_channel(1067177909657288804)
        embed = discord.Embed(description=message.content,color=0xff0000) 
        embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id,message.author.avatar))
        embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
        await channel.send(embed=embed)
        await message.delete()
        return
    await message.add_reaction('<a:b_sending:1108227693230702642>')
    for channel in client.get_all_channels(): #BOTが所属する全てのチャンネルをループ
        if channel.name == chat_name: #グローバルチャット用のチャンネルが見つかったとき
            if channel == message.channel: #発言したチャンネルには送らない
                continue
            embed=discord.Embed(description=message.content, color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            if message.attachments != []: #添付ファイルが存在するとき
                embed.set_image(url=message.attachments[0].url)

            if message.reference: #返信メッセージであるとき
                reference_msg = await message.channel.fetch_message(message.reference.message_id) #メッセージIDから、元のメッセージを取得
                if reference_msg.embeds and reference_msg.author == client.user: #返信の元のメッセージが、埋め込みメッセージかつ、このBOTが送信したメッセージのとき→グローバルチャットの他のサーバーからのメッセージと判断
                    reference_message_content = reference_msg.embeds[0].description #メッセージの内容を埋め込みから取得
                    reference_message_author = reference_msg.embeds[0].author.name #メッセージのユーザーを埋め込みから取得
                elif reference_msg.author != client.user: #返信の元のメッセージが、このBOTが送信したメッセージでは無い時→同じチャンネルのメッセージと判断
                    reference_message_content = reference_msg.content #メッセージの内容を取得
                    reference_message_author = reference_msg.author.name+'#'+reference_msg.author.discriminator #メッセージのユーザーを取得
                reference_content = ""
                for string in reference_message_content.splitlines(): #埋め込みのメッセージを行で分割してループ
                    reference_content += "> " + string + "\n" #各行の先頭に`> `をつけて結合
                reference_value = "**@{}**\n{}".format(reference_message_author, reference_content) #返信メッセージを生成
            embed.add_field(name='返信しました', value=reference_value, inline=True) #埋め込みに返信メッセージを追加
            
            await channel.send(embed=embed) #メッセージを送信
        await message.remove_reaction('<a:b_sending:1108227693230702642>', client.user)
        await message.add_reaction('<a:b_send_check:1111885505794166865>') #リアクションを送信
        # 5秒待ってからリアクションを削除する
        await asyncio.sleep(4)
        await message.remove_reaction('<a:b_send_check:1111885505794166865>', client.user)
