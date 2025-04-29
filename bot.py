import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

# إعداد البوت مع الصلاحيات المطلوبة
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# إنشاء كائن البوت
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.command()
async def ping(ctx):
    """اختبار بسيط للتأكد من أن البوت يعمل"""
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def members(ctx):
    """عرض عدد الأعضاء في السيرفر"""
    await ctx.send(f'عدد الأعضاء في السيرفر: {ctx.guild.member_count}')

# تشغيل البوت
TOKEN = os.getenv('DISCORD_TOKEN')  # قراءة التوكن من ملف .env
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: No token found. Please set DISCORD_TOKEN in .env file") 