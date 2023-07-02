# Discord Image Scraper

Discord Image Scraper is a Python-based bot that listens for image attachments in a specific Discord channel and downloads them to your local machine. It uses the discord.py.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This bot requires Python 3.8 or newer, and uses several Python libraries including discord.py and python-dotenv.

To install Python, follow the instructions at [python.org](https://www.python.org/downloads/).

You will also need to install the required Python libraries. In your command line, navigate to the directory containing the bot files, then run:

```
pip install -r requirements.txt
```

### Installing

After cloning the repository and installing the prerequisites, you'll need to set up a .env file in the same directory as the bot. This file should contain the following:

```
TOKEN='your-bot-token'
GUILD_ID='your-guild-id'
CHANNEL_ID='your-channel-id'
```

Replace 'your-bot-token' with your bot's token, 'your-guild-id' with the ID of your Discord guild (server), and 'your-channel-id' with the ID of the channel you want the bot to monitor.

Once your .env file is set up, you can run the bot from the command line using:

```
python ens-scraper.py
```

This will run the bot and drop the images in the current date's folder.

## Built With

* [Python 3](https://www.python.org) - The programming language used
* [discord.py](https://discordpy.readthedocs.io/en/stable/) - The main library used to interact with Discord's API
* [python-dotenv](https://github.com/theskumar/python-dotenv) - Library used to load environment variables from .env file
