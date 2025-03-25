from dotenv import load_dotenv
import os 

import discord
from discord.ext import commands 
from discord import app_commands 

import spotapi
import spotifyapi
import spotify_api_key_gen

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
# api_key = spotify_api_key_gen.get_token()
guild_id = discord.Object(id=os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    try:
        synced = await client.tree.sync(guild=guild_id)
        print(f'Synced {len(synced)} commands to guild {guild_id}')
    except Exception as e:
        print(f'Error syncing commnds: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('hello'):
        await message.channel.send(f'Hello, {message.author}')

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send('You reacted')

@client.tree.command(name="hello", description="Say hello!", guild=guild_id)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="playlist_view", description="Will print spotify playlist", guild=guild_id)
async def viewPlaylist(interaction: discord.Interaction, playlist_url: str):
    await interaction.response.send_message("Fetching playlist...")

    playlist_size = spotifyapi.size_of_playlist(playlist_url)
    str_to_return = ""

    for i in range(playlist_size):
        str_to_return += str(i) + "\t" + spotifyapi.get_playlist_song(playlist_url, i) + "\n"

    await interaction.followup.send(str_to_return + "\nDone!")

client.run(bot_token)