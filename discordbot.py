import discord
import random
import openai
import os

# Replace 'discord' import with this to get access to the intents
from discord.ext import commands

# Your bot token goes here
TOKEN = "MTExNTk1MTYxOTk4MTQ1OTQ5Ng.GLfrnl.-MFe-r-6wgvNcsXuyByEv9cxVUr9bHa4TBmj0A"

# Define the intents your bot requires
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with intents
bot = commands.Bot(command_prefix='8', intents=intents)

# Your GPT-3.5 API key goes here
GPT_API_KEY = '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'

# Name of the requirements file
REQUIREMENTS_FILE = 'REQUIREMENTS.txt'

# Intents for your bot (you can customize these based on your bot's needs)
intents = discord.Intents.default()
intents.message_content = True

# Initialize the Discord client with intents
client = discord.Client(intents=intents)

# Set up the GPT-3.5 API client
openai.api_key = GPT_API_KEY

# Function to install Python dependencies from the REQUIREMENTS_FILE
def install_dependencies():
    os.system(f"/usr/local/bin/python -m pip install -U -r {REQUIREMENTS_FILE}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # Install Python dependencies on bot startup
    install_dependencies()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')
    elif message.content.startswith('!Rader'):
        await message.channel.send('RADER IS MY DADDY!')
    elif message.content.startswith('!Info'):
        await message.channel.send('a simple bot made by raders!')
    elif message.content.startswith('!update'):
        await message.channel.send('when we update we will update but rn we are on version 1.51!')
    elif message.content.startswith('!users'):
        random_number = random.randint(3,25 )
        await message.channel.send(f'Users on Lua rn: {random_number}')
    elif message.content.startswith('/radergpt'):
        # Get the question from the user's message
        question = message.content[len('/radergpt'):].strip()

        if not question:
            await message.channel.send("Please provide a question after the command, like this: `/radergpt What is the capital of France?`")
            return

        try:
            # Call the GPT-3.5 API to get the answer
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=question,
                max_tokens=150
            )

            # Get the answer from the GPT-3.5 API response
            answer = response.choices[0].text.strip()

            # Send the answer back to the Discord channel
            await message.channel.send(f"**Answer:** {answer}")

        except Exception as e:
            await message.channel.send(f"An error occurred while processing the question: {str(e)}")

client.run(TOKEN)
