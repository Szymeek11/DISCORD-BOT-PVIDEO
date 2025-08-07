import discord, os
from dotenv import load_dotenv as l
from e.ev import m

l()
t = os.getenv("token")
ka = int(os.getenv("ka"))

i = discord.Intents.default()
i.message_content = True
k = discord.Client(intents=i)

k.event(m(k, ka))
k.run(t)
