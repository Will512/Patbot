# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:03:02 2021

@author: schmi
"""

import os
from discord.ext import commands
from discord.utils import get
import discord
from dotenv import load_dotenv
import random
import requests


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PATID_DISC = 331046481798758400
MWID_DISC = 330516055153704960
def auth():
    return os.getenv('BEARER_TOKEN')

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
client = discord.client()
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="?askpat help"))
# @bot.command(name='help',help = 'Displays all available commands')
# async def help(ctx):
#     return
@client.event
async def on_message(message):
    author = message.author
    if author.id == MWID_DISC:
        await client.send_message(message.channel, f"Aight {author}")
        emoji = get(bot.get_all_emojis(), name='pat')
        await client.add_reaction(message,emoji)

@bot.command(name='song',help = 'Plays a random Pat song')
async def song(ctx):
    songs = ['kumbaya','ed sheeran rap','firework katy perry','big time rush by big time rush (album = btr)' ]
    response = '-play ' + random.choice(songs)
    await ctx.send(response)
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
              "People on this subreddit hate askpat13. The first question to ask: why? Why do you all hate him? The obvious answer: you didn't watch him in his prime."]
    response = random.choice(pastas)
    await ctx.send(response)
bot.run(TOKEN)