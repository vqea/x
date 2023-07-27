import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"connected to {bot.user.name}")
    
    
@bot.command()
async def rates(ctx):
    x = ctx.guild.name
    y = ctx.guild.icon.url
    z = "https://cdn.discordapp.com/attachments/1133423979659546755/1134114948478410812/llll.png"
    ca = "<:cashapp:1134123689357615195>"
    pp = "<:paypal:1134123735499161694>"
    cr = "<:crypto:1134123606209724477>"
    emb = discord.Embed(
        title="exchange rates",
        description=f"""_ _
{ca} <-> {pp}
_8% fee, $2 min_

{ca} <-> {cr}
_7% fee, $2 min_

{pp} <-> {cr}
_8% fee, $2 min_

{cr} <-> {cr}
_3% fee, $1 min_
        """
    )
    emb.set_author(
        name=x,
        icon_url=y
    )
    emb.set_image(url=z)
    emb.set_thumbnail(url=y)
    await ctx.message.delete()
    await ctx.send(embed=emb)


@bot.command()
async def update(ctx, amount: int=None):
    c = bot.get_channel(1134106690342621234)
    old = c.name
    new = int(old) + amount
    c.edit(name=new)
    e = discord.embed(color=0xffffff, description="updated total amount exchanged to `${new}`")
    
bot.run("MTEzMzUxMTI2MTA5MTU0MTAwMg.GRje1C.vO-U0tj2-NBGmflWc6W7gEjZuqkuOKoeLy9Yr0")
