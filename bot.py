import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

MESSAGE_TEXT = """
**🔥 Robux Gifter Prices 🔥**

**🗓️ 1 Week Key** → **$10 USD**
**📆 1 Month Key** → **$15 USD**
**♾️ Lifetime Key** → **$25 USD**

⚡ Fast Delivery
✅ Trusted Service
💰 More Robux, More Fun!

**💸 Payment Methods:**

• 🟢 PayPal
• 💜 Discord Nitro
• 🎮 Robux

**✅ Pick your payment method when opening a ticket!**
"""

@bot.event
async def on_ready():
    print(f'✅ Bot ist online als {bot.user}')
    
    channel_id = 1512558400569872434   # ← Deine Kanal ID hier

    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send(MESSAGE_TEXT)
        print(f"✅ Nachricht in #{prices} gesendet!")
    else:
        print("❌ Kanal nicht gefunden!")

bot.run("MTUxMjU2ODg0MjM2OTM3MjI0MQ.G8h1NG.0HbxSA4OviqMsiZtRr-hmMAVDKkZKMb7OTkOgE")