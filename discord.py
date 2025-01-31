import discord
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = ''
# Replace 'CHANNEL_ID' with the ID of your target channel
CHANNEL_ID =   # e.g., 123456789012345678

client = discord.Client()

# List of messages to send
messages = [
    "Science is organized knowledge, wisdom is organized life.
", "Sahara vibes are strong let's keep exploring
", "i hope
", # Add up to 50 messages
]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    while True:
        for message in messages:
            await channel.send(message)
            await asyncio.sleep(300)  # Wait for 60 seconds before sending the next message

client.run(TOKEN)
