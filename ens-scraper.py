import discord
from discord.ext import commands
from datetime import datetime
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

TOKEN = os.getenv('TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    logging.info(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.guild.id == GUILD_ID and message.channel.id == CHANNEL_ID:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    folder_name = datetime.now().strftime('%Y-%m-%d')
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                        logging.info(f'Created new directory: {folder_name}')

                    file_name = f"{message.author.name}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')}"
                    file_path = os.path.join(
                        folder_name, file_name + os.path.splitext(attachment.filename)[1])

                    await attachment.save(file_path)
                    logging.info(f'Saved file: {file_path}')

bot.run(TOKEN)
