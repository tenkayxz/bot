
import discord
import os
import asyncio
import random
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Mensagens estranhas / analog horror
mensagens = [
    "você está vendo isso também?",
    "não olhe para trás.",
    "ele está chegando...",
    "01001000 01101111 01101100 01100001",
    "eu vi você desconectar... mas você nunca saiu.",
    "o sinal caiu. mas eu ainda te escuto.",
    "a quanto tempo eu estou aqui dentro",
]

async def mandar_mensagem_aleatoria():
    await bot.wait_until_ready()
    canal_id = int(os.getenv("DISCORD_CHANNEL_ID"))  # Canal onde vai enviar
    canal = bot.get_channel(canal_id)

    if not canal:
        print("Canal não encontrado. Verifique o ID.")
        return

    while not bot.is_closed():
        mensagem = random.choice(mensagens)
        await canal.send(mensagem)

        tempo = random.randint(1800, 10800)  # entre 30 min e 3h
        await asyncio.sleep(tempo)

@bot.event
async def setup_hook():
    bot.loop.create_task(mandar_mensagem_aleatoria())
    
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

bot.run(TOKEN)
