# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:03:02 2021

@author: schmi
"""

import os
from discord.ext import commands
#from discord.utils import get
import discord
#from dotenv import load_dotenv
import random
import requests
import youtube_dl


#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'ODA5NDQ5MjY3Njk3MTU2MTA2.YCVQYA.6Fltu3XBr8syPiPqtlzENQ2NUc0'
PATID_DISC = 331046481798758400
MWID_DISC = 330516055153704960
WSID_DISC = 337440868669849600


#PAT_EMOJI_ID = 809672961296433153
PAT_EMOJI_ID =754023549483745402
def auth():
    #return os.getenv('BEARER_TOKEN')
    return 'AAAAAAAAAAAAAAAAAAAAAI7AMgEAAAAAR75daqRdXYm6EEVXrm3KJbH%2Fh2I%3DjA34LmjiG5nzWr5s0IrFusX3NNJRGomnfj58P6Ab6X8fhZ034k'

def create_url():
    query = "from:askpat13"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    #print(url)
    return url
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers
def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
def getID():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    ret = json_response["data"][0]["id"]
    return ret

bot = commands.Bot(command_prefix='?askpat ')
client = discord.Client()
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="?askpat help"))
    #for emoji in bot.emojis:
       # print("Name:", emoji.name + ",", "ID:", emoji.id)
# @bot.command(name='help',help = 'Displays all available commands')
# async def help(ctx):
#     return
@bot.event
#@bot.event()
async def on_message(message):
    if(message.author != client.user):
        await bot.process_commands(message)
        author = message.author.id
        #print(author)
        if(author== PATID_DISC):
        #if(author== PATID_DISC or author==WSID_DISC):
            #await message.channel.send("I'm a sick fuck I like a quick Fuck WOO!")
            #emoji = get(bot.get_all_emojis(), name='pat')
            #emoji = discord.ext.commands.Bot.get_emoji(id = PAT_EMOJI_ID)
            emoji = bot.get_emoji(PAT_EMOJI_ID)
            await message.add_reaction(emoji)
        

@bot.command(name='song',help = 'Plays a random Pat song')
async def song(ctx, url: str):
    # songs = ['kumbaya','ed sheeran rap','firework katy perry','big time rush by big time rush (album = btr)' ]
    # response = '-play ' + random.choice(songs)
    # await ctx.send(response)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
@bot.command(name='arushi',help='...')
async def arushi(ctx):
    await ctx.send('Come on guys, I already told you we\'re just friends')
@bot.command(name = 'tweet',help='Displays Pat\'s most recent twitter activity.')
async def tweet(ctx):
    tweet = 'https://www.twitter.com/askpat13/status/' + str(getID())
    await ctx.send(tweet)
@bot.command(name='pasta',help='Display a random Pat copypasta')
async def pasta(ctx):
    pastas = ["if AskPat13 has million number of fans i am one of them. if AskPat13 has ten fans i am one of them. if AskPat13 has no fans. that means i am no more on the earth. if world against AskPat13, i am against the world. i love AskPat13 till my last breath... die hard fan of AskPat13.",
              "Look here, I'm askpat13's computer.  You may put slander on my name, but don't you EVER put slander on my owner.  Askpat13 has been a great person and owner.  He has kept me safe and even opened me up and replace my random access memory.  He's built different, and I'M BUILT DIFFERENT",
              "My name is AskPat13 and you may ask me about if I'm pat or if I'm actually 13, but truthfully I'm neither. I'm a winner, and always have been.  I've played this whole game with no monitor and one handed, naked in my dorm. Imagine what I can do clothed, two handed, and full strength.",
              "SPAM :kissing_cat: THIS :kissing_cat: CAT :kissing_cat: TO :kissing_cat: ASK :kissing_cat: PAT",
              "I’m telling you, askpat is as cracked as he is jacked. I saw him at a 7-11 the other day buying Monster and adult diapers. I asked him what the diapers were for and he said ”they contain my full power so I don’t completely shit on these kids“ then he aerialed out the door",
              "People on this subreddit hate askpat13. The first question to ask: why? Why do you all hate him? The obvious answer: you didn't watch him in his prime.",
              "I'm pro sandwich - askpat13"]
    response = random.choice(pastas)
    await ctx.send(response)
bot.run(TOKEN)
#client.run(TOKEN)