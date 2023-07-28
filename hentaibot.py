import os
import random
from hentai_func import Hentai, NekosFunTags, NsfwApis
import discord
from discord import app_commands
from typing import Optional
from dotenv import load_dotenv
from datetime import datetime


class Bot(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


intents = discord.Intents(messages=True, members=True, typing=True, guilds=True)
bot = Bot(intents=intents)
game = discord.Game("Naughty")

load_dotenv()
token = os.getenv("token")


@bot.event
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.tree.command(description="Shows the help menu", nsfw=True)
async def help(ctx: discord.Interaction):
    await ctx.response.defer()
    ret = "```\n"
    ret += "rule34 [tags]\n"
    ret += "Get image/video from Rule34 (EXTREME CONTENT AHEAD!!!).\n"    
    ret += "gelbooru [tags]\n"
    ret += "Get image/video from Gelbooru\n"
    ret += "yandere [tags]\n"
    ret += "Get image from Yande.re\n"
    ret += "konachan [tags]\n"
    ret += "Get image from Konachan\n"
    ret += "danbooru [tags]\n"
    ret += "Get image/video from Danbooru\n"    
    ret += "nekosfun [tag]\n"
    ret += "Get images/gifs from NekosLife\n"
    ret += "boobchi\n"
    ret += "Get a random ecchi image of Hitori Gotoh\n\n"    
    ret += "TAG FORMATTING:\n"
    ret += "Using `,` after adding another tag turns to `+` and leaving a space turn some tags to `_`."
    ret += "```"
    await ctx.followup.send(ret)

@bot.tree.command(description="Get hentai from Rule34 (EXTREME!!!)", nsfw=True)
@app_commands.describe(tag="Add a tag")
async def rule34(ctx: discord.Interaction, tag: Optional[str] = None) -> None:
    await ctx.response.defer()
    ret = await Hentai().get_nsfw_image(NsfwApis.Rule34Api, tag)
    source = ret["source"]
    owner = ret["owner"]
    score = ret["score"]
    image = ret["file_url"]
    if image.endswith(".mp4"):
        await ctx.followup.send(image)
    else:
        embed = discord.Embed(title="Created by {}".format(owner))
        embed.color=discord.Color.random()
        if source != "":
            embed.add_field(
                name="Source", value="[Click here]({})".format(source), inline=True
            )
        embed.add_field(name="Score", value=score, inline=True)
        embed.set_image(url=image)
        embed.set_footer(text="Fetched from Rule34")
        await ctx.followup.send(embed=embed)

@bot.tree.command(description="Get hentai from Gelbooru", nsfw=True)
@app_commands.describe(tag="Add a tag")
async def gelbooru(ctx: discord.Interaction, tag: Optional[str] = None) -> None:
    await ctx.response.defer()
    ret = await Hentai().get_nsfw_image(NsfwApis.GelbooruApi, tag)
    source = ret["source"]
    owner = ret["owner"]
    score = ret["score"]
    image = ret["file_url"]
    created_at = ret["created_at"]
    if image.endswith(".mp4"):
        await ctx.followup.send(image)
    else:
        embed = discord.Embed(title="Created by {}".format(owner))
        embed.color=discord.Color.random()
        if source != "":
            embed.add_field(
                name="Source", value="[Click here]({})".format(source), inline=True
            )
        embed.add_field(name="Score", value=score, inline=True)
        embed.set_image(url=image)
        embed.set_footer(text="Fetched from Gelbooru\nCreated at {}".format(created_at))
        await ctx.followup.send(embed=embed)


@bot.tree.command(description="Get hentai from Yandere", nsfw=True)
@app_commands.describe(tag="Add a tag")
async def yandere(ctx: discord.Interaction, tag: Optional[str] = None) -> None:
    await ctx.response.defer()
    ret = await Hentai().get_nsfw_image(NsfwApis.YandereApi, tag)
    created_at = datetime.fromtimestamp(int(ret["created_at"]))
    file = ret["file_url"]
    author = ret["author"]
    source = ret["source"]
    score = ret["score"]
    embed = discord.Embed(title="Created by {}".format(author))
    embed.color=discord.Color.random()
    if source != "":
        embed.add_field(
            name="Source", value="[Click here]({})".format(source), inline=True
        )
    embed.add_field(name="Score", value=score, inline=True)
    embed.set_image(url=file)
    embed.set_footer(text="Fetched from Yande.re\nCreated at {}".format(created_at))
    await ctx.followup.send(embed=embed)


@bot.tree.command(description="Get hentai from Konachan", nsfw=True)
@app_commands.describe(tag="Add a tag")
async def konachan(ctx: discord.Interaction, tag: Optional[str] = None) -> None:
    await ctx.response.defer()

    ret = await Hentai().get_nsfw_image(NsfwApis.KonachanApi, tag)

    created_at = datetime.fromtimestamp(int(ret["created_at"]))
    file = ret["file_url"]
    author = ret["author"]
    source = ret["source"]
    score = ret["score"]
    embed = discord.Embed(title="Created by {}".format(author))
    embed.color=discord.Color.random()
    if source != "":
        embed.add_field(
            name="Source", value="[Click here]({})".format(source), inline=True
        )
    embed.add_field(name="Score", value=score, inline=True)
    embed.set_image(url=file)
    embed.set_footer(text="Fetched from Konachan\nCreated at {}".format(created_at))
    await ctx.followup.send(embed=embed)


@bot.tree.command(description="Get hentai from Danbooru", nsfw=True)
@app_commands.describe(tag="Add a tag")
async def danbooru(ctx: discord.Interaction, tag: Optional[str] = None) -> None:
    await ctx.response.defer()
    ret = await Hentai().get_nsfw_image(NsfwApis.DanbooruApi, tag)
    created_at = ret["created_at"]
    file = ret["file_url"]
    ret["source"]
    author = ret["tag_string_artist"]
    source = ret["source"]
    score = ret["score"]
    embed = discord.Embed(title="Created by {}".format(author))
    embed.color=discord.Color.random()
    if source != "":
        embed.add_field(
            name="Source", value="[Click here]({})".format(source), inline=True
        )
    embed.add_field(name="Score", value=score, inline=True)
    embed.set_image(url=file)
    embed.set_footer(text="Fetched from Danbooru\nCreated at {}".format(created_at))
    await ctx.followup.send(embed=embed)


@bot.tree.command(description="Get an image/gif from NekosLife", nsfw=True)
@app_commands.describe(tag="Which tag?")
async def nekosfun(ctx: discord.Interaction, tag: Optional[NekosFunTags]) -> None:
    await ctx.response.defer()
    tag = tag if tag else random.choice(list(NekosFunTags))
    image = Hentai.nekofun(tag.value)

    if image == False:
        await ctx.followup.send("An error has occurred!")
    else:
        embed = discord.Embed()
        embed.color=discord.Color.random()
        embed.set_image(url=image)
        embed.set_footer(text="Fetched from Nekos.Fun")
        await ctx.followup.send(embed=embed)

@bot.tree.command(description="Get a random ecchi image of Hitori Gotoh")
async def boobchi(ctx:discord.Interaction):
    await ctx.response.defer()
    image, source = Hentai.boobchi()

    if image == False:
        await ctx.followup.send("An error has occurred!")
    else:
        embed = discord.Embed()
        embed.color=discord.Color.random()
        embed.description=f"[Source]({source})"
        embed.set_image(url=image)
        embed.set_footer(text="Fetched from Bocchi-API")
        await ctx.followup.send(embed=embed)    


@bot.tree.error
async def on_app_command_error(
    ctx: discord.Interaction, error: app_commands.errors.AppCommandError
):
    if isinstance(error, app_commands.errors.CommandInvokeError) and isinstance(error.original, (IndexError, TypeError, KeyError)):
        embed = discord.Embed(
            title="Hentai Failed",
            description="Hentai couldn't be sent in this channel",
            color=0xFF0000,
        ).add_field(name="Reason", value="Tag not found or hentai could not be found")
        await ctx.followup.send(embed=embed)


bot.run(token)
