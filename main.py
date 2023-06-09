import discord
import os
import asyncio
import datetime
import sys
import json
import customgc
from discord_slash import SlashCommand, SlashContext
from discord.ext import commands

global_channel_name = "レギオンチャットの集まり" #設定したいチャンネル名を入力
client = discord.Client() #接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='gc!')
#slash = SlashCommand(client, sync_commands=True)
slash = SlashCommand(client, sync_commands=False)

block_word1 = 'discord.gg'
block_word2 = 'しね'
block_word3 = '死ね'
block_word4 = '@everyone'
block_word5 = '@here'
ban_list = {}

#モデレーターのID
special_user_ids = [862605548389269525, 843614879234392104, 824169770949541929]
#レギオン上層部のID
legion_reader_ids = [
                    872343576468656208, 937941870254891019, 962335888443047986, 880848532880384000, 872705736390623373, 
                    719495146466574347, 708992909256687617, 724305956913283154, 749520172917850183, 947161562827878451, 
                    755626031594864711
                    ]
#導入が許可されてるサーバーID
guild_passids = [
                964126234734911560, 927192946288230410, 1072722339822837781, 1013965449949626378, 838319926309289994, 991197674827153438
                ]

#スラッシュコマンド
@slash.slash(name="gc-help", description="グローバルチャットの利用方法についてはこのコマンドをご利用ください。")
async def help(ctx: SlashContext):
        embed = discord.Embed(title="ズミン！グローバルチャットヘルプ",description="グローバルチャットの詳細は、こちらの[webサイト](https://bit.ly/3WU6LER)で確認できます。\n不具合報告はこちらのフォームをご利用ください。[不具合報告フォーム](https://forms.gle/dNRaLcpCrR6bCo7o8)",color=0x9B95C9) 
        await ctx.send(embed=embed)
        
@slash.slash(name='gc_ban', description='グローバルチャットからユーザーをBANします。')
async def gc_ban(ctx, user: discord.User):
    server_id = ctx.author.id
    target_server_id = [862605548389269525, 843614879234392104, 824169770949541929]  # 目標のサーバーID

    if server_id in target_server_id:
    # JSONデータベースからBANリストを読み込む
        with open('zumin-gloval/banlist.json', 'r') as f:
           banlist = json.load(f)

    # ユーザーをBANリストに追加
        banlist.append(user.id)

    # BANリストをJSONデータベースに保存
        with open('zumin-gloval/banlist.json', 'w') as f:
            json.dump(banlist, f)

        await ctx.send(f'<@{user.id}> このユーザのグローバルチャットBANを実行しました。')
        pass
    else:
        await ctx.send("このコマンドを実行する権限はありません！")
        pass

@slash.slash(name='gc_unban', description='グローバルチャットのBANを解除します。')
async def gc_unban(ctx, user: discord.User):
    server_id = ctx.author.id
    target_server_id = [862605548389269525, 843614879234392104, 824169770949541929]  # 目標のサーバーID/サーバーって書いてあるけど実際はユーザーIDです変えるのめんどくさかった

    if server_id in target_server_id:
    # JSONデータベースからBANリストを読み込む
        with open('zumin-gloval/banlist.json', 'r') as f:
            banlist = json.load(f)

    # ユーザーをBANリストから削除
        if user.id in banlist:
            banlist.remove(user.id)
            await ctx.send(f'<@{user.id}> このユーザのグローバルチャットBANを解除しました。')
        else:
            await ctx.send(f'<@{user.id}> このユーザーはBANされていません。\nBANされていないユーザーをUnBANすることはできません。')
        pass
    else:
        await ctx.send("このコマンドを実行する権限はありません！")
        pass

    # BANリストをJSONデータベースに保存
    with open('zumin-gloval/banlist.json', 'w') as f:
        json.dump(banlist, f)

@slash.slash(name="gc_debug", description="botの情報を取得します。")
async def gc_debug(ctx: SlashContext):
    
    num_of_servers = len(client.guilds)
    # Ping値を秒単位で取得
    raw_ping = client.latency
    # ミリ秒に変換して丸める
    ping = round(raw_ping * 1000)
    
    embed=discord.Embed(title="ズミン！グローバルチャット！#7319 bot info", color=0x00fa1d)
    embed.set_author(name="ズミン！グローバルチャット！#7319", icon_url="https://cdn.discordapp.com/avatars/1062307568262840380/5e3e9df3fa9f7165f89933c35bae71f6.png?size=4096")
    embed.add_field(name="所属しているサーバーの数:", value=num_of_servers, inline=True)
    embed.add_field(name="コマンドping", value=f"**{ping}ms**")
    await ctx.send(embed=embed)
    
@client.event
async def on_message(message):
    if message.channel.name == global_channel_name:
        with open('zumin-gloval/banlist.json', 'r') as file:
            banlist = json.load(file)
    
        user_id = message.author.id
    
        if user_id in banlist:
            await message.add_reaction('<:error:1041554270958387220>')
            await message.delete()
            embed = discord.Embed(title="お知らせ", description="現在、あなたは利用制限を受けているため、グローバルチャットの利用ができません。", color=0xff0000) 
            await message.author.send(embed=embed)
            return
        
        if message.author.id == client.user.id:
            return
        
        await message.add_reaction('<a:b_sending:1108227693230702642>')
        
        if message.content.find(block_word1) != -1:
            await message.author.send('Discordサーバーの宣伝行為は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content, color=0xff0000) 
            emoji_url = '絵文字のURL'
            if message.author.id == '特定のユーザーのID':
                embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator), icon_url=emoji_url)
            else:
                embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator), icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id), icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
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
        # メッセージを送信
        
        for channel in client.get_all_channels():
            if channel.name == global_channel_name:
                if channel == message.channel:
                    continue
                embed = discord.Embed(description=message.content, color=0x9B95C9)
                if message.author.nick is not None:
                    name = message.author.nick
                else:
                    name = message.author.name
                if message.author.id in special_user_ids:
                    embed.set_author(name=f"{name}👑", icon_url=f"https://media.discordapp.net/avatars/{message.author.id}/{message.author.avatar}.png?size=1024")
                elif message.author.id in legion_reader_ids:
                    embed.set_author(name=f"{name}🍀", icon_url=f"https://media.discordapp.net/avatars/{message.author.id}/{message.author.avatar}.png?size=1024")
                elif message.author.bot:
                    embed.set_author(name=f"{name}🤖", icon_url=f"https://media.discordapp.net/avatars/{message.author.id}/{message.author.avatar}.png?size=1024")
                else:
                    embed.set_author(name=f"{name}", icon_url=f"https://media.discordapp.net/avatars/{message.author.id}/{message.author.avatar}.png?size=1024")
                embed.set_footer(text=f"{message.guild.name} / UserID:{message.author.id}", icon_url=f"https://media.discordapp.net/icons/{message.guild.id}/{message.guild.icon}.png?size=1024")
                if message.attachments != []: #添付ファイルが存在するとき
                    embed.set_image(url=message.attachments[0].url)

                if message.reference: #返信メッセージであるとき
                    reference_msg = await message.channel.fetch_message(message.reference.message_id) #メッセージIDから、元のメッセージを取得
                    if reference_msg.embeds and reference_msg.author == client.user: #返信の元のメッセージが、埋め込みメッセージかつ、このBOTが送信したメッセージのとき→グローバルチャットの他のサーバーからのメッセージと判断
                        reference_message_content = reference_msg.embeds[0].description #メッセージの内容を埋め込みから取得
                        reference_message_author = reference_msg.embeds[0].author.name #メッセージのユーザーを埋め込みから取得
                    elif reference_msg.author != client.user: #返信の元のメッセージが、このBOTが送信したメッセージでは無い時→同じチャンネルのメッセージと判断
                        reference_message_content = reference_msg.content #メッセージの内容を取得
                        reference_message_author = reference_msg.author.name #メッセージのユーザーを取得
                    reference_content = ""
                    for string in reference_message_content.splitlines(): #埋め込みのメッセージを行で分割してループ
                        reference_content += "> " + string + "\n" #各行の先頭に`> `をつけて結合
                    reference_value = "**@{}**\n{}".format(reference_message_author, reference_content) #返信メッセージを生成
                    embed.add_field(name='返信しました', value=reference_value, inline=True) #埋め込みに返信メッセージを追加
                
                await channel.send(embed=embed)
        
        await message.remove_reaction('<a:b_sending:1108227693230702642>', client.user)
        await message.add_reaction('<a:b_send_check:1111885505794166865>')
        await asyncio.sleep(4)
        await message.remove_reaction('<a:b_send_check:1111885505794166865>', client.user)
                
    else:
        return
    
@client.event
async def on_guild_join(guild):
    if guild.id in guild_passids:
        channel = client.get_channel(1067177909657288804)
        embed=discord.Embed(title="新規bot参加", description=f"Botが「{guild.name}」に参加しました。", color=0x00ffe1)
        embed.set_footer(text=f"GuildID:{guild.id}", icon_url=guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
    else:
        await guild.leave()
        return
    
@client.event
async def on_voice_state_update(member, before, after):
    specific_channel_id = 1111308842488307752
    message_channel_id = 964126235494084640
    sp_channel = 1107889259714707466

    if before.channel == after.channel:
        return

    if after.channel and after.channel.id == specific_channel_id:
        guild = member.guild
        specific_channel = guild.get_channel(specific_channel_id)
        message_channel = guild.get_channel(message_channel_id)
        if before.channel.id != sp_channel:
            await message_channel.send(f'<#{before.channel.id}>に寝落ちしている人がいたから<@{member.id}>を食べちゃったガオ♪\nとってもおいしかったガオ♪')
        else:
            await message_channel.send(f'<#{before.channel.id}>においしそうな人がいたから<@{member.id}>を食べちゃったガオ♪\nとってもおいしかったガオ♡')
    else:
        return
    
@client.event
async def on_ready():
    
    game = discord.Game(f'空島上空を飛行中！')
    await client.change_presence(status=discord.Status.online, activity=game)
    print('ログインしました')
    print('------')
    print(client.user.name)  # Botの名前
    print(discord.__version__)  # discord.pyのバージョン
    print('------')

client.run("Your Token here")
