import discord

TOKEN = "token" #トークンを入力
global_channel_name = "channel-name" #設定したいチャンネル名を入力

client = discord.Client() #接続に必要なオブジェクトを生成
block_word1 = 'discord.gg'
block_word2 = 'しね'
block_word3 = '死ね'
block_word4 = 'everyone'
block_word5 = 'here'
block_user = ''
timeout_user = ''

@client.event
async def on_message(message):

    if message.channel.name == global_channel_name: #グローバルチャットにメッセージが来たとき
        #メッセージ受信部
        if message.author.id == client.user.id: #BOTの場合は何もせず終了
            return
        #メッセージをブロック
        if  message.content.find(block_word1) != -1:
            await message.author.send('ブロックされた単語の送信は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content,color=0xff0000) 
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            await channel.send(embed=embed)
            return
        if  message.content.find(block_word2) != -1:
            await message.author.send('ブロックされた単語の送信は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content,color=0xff0000) 
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            await channel.send(embed=embed)
            return
        if  message.content.find(block_word3) != -1:
            await message.author.send('ブロックされた単語の送信は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content,color=0xff0000) 
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            await channel.send(embed=embed)
            return
        if  message.content.find(block_word4) != -1:
            await message.author.send('ブロックされた単語の送信は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content,color=0xff0000) 
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            await channel.send(embed=embed)
            return
        if  message.content.find(block_word5) != -1:
            await message.author.send('ブロックされた単語の送信は許可されていません！')
            await message.add_reaction('<:error:1041554270958387220>')
            channel = client.get_channel(1067177909657288804)
            embed = discord.Embed(description=message.content,color=0xff0000) 
            embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
            embed.set_footer(text="{} / UserID:{}".format(message.guild.name, message.author.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
            await channel.send(embed=embed)
            return
        
        #メッセージ送信部
        for channel in client.get_all_channels(): #BOTが所属する全てのチャンネルをループ
            if channel.name == global_channel_name: #グローバルチャット用のチャンネルが見つかったとき
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
        await message.add_reaction('<:check:1043897762590236704>') #リアクションを送信
        
@client.event
# BOTが起動したときに発火するイベント 'on_ready'
async def on_ready():
    
    game = discord.Game(f'空島上空を飛行中！')
    # f文字列(フォーマット済み文字列リテラル)は、Python3.6からの機能です。
    
    # BOTのステータスを変更する
    await client.change_presence(status=discord.Status.online, activity=game)
    # パラメーターの status でステータス状況(オンライン, 退席中など)を変更できます。
    
    print('ログインしました')
    print(client.user.name)  # Botの名前
    print(client.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


client.run(TOKEN)
