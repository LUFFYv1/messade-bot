import discord
import os
from discord.ext import commands

TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")


# ---------------- SAY ----------------

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)


# ---------------- EMBED ----------------

@bot.command()
async def embed(ctx, title, *, message):

    emb = discord.Embed(
        title=title,
        description=message,
        color=discord.Color.blue()
    )

    emb.set_footer(text="AZ Message Bot")

    await ctx.send(embed=emb)


# ---------------- PHOTO ----------------

@bot.command()
async def photo(ctx, url):

    emb = discord.Embed(title="AZ ESPORTS")

    emb.set_image(url=url)

    await ctx.send(embed=emb)


# ---------------- LINK ----------------

@bot.command()
async def link(ctx, url):

    await ctx.send(url)


bot.run(TOKEN)
