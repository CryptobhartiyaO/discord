import discord
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = 'MTMzNDg5MTU2NDI1Nzc3NTcxNg.GXFisW.LbaU3Z-dOwCnvBLY0qPyMQvi-EVasnf7n5jffQ'
# Replace 'CHANNEL_ID' with the ID of your target channel
CHANNEL_ID = 1209630079936630824  # e.g., 123456789012345678

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