import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"connected to {bot.user.name}")
    await bot.change_presence(activity=discord.Streaming(name="exchanges", url="https://twitch.tv/x"))
    
    
@bot.command()
@commands.is_owner()
async def rates(ctx):
    x = ctx.guild.name
    y = ctx.guild.icon.url
    z = "https://cdn.discordapp.com/attachments/1133423979659546755/1134114948478410812/llll.png"
    ca = "<:cashapp:1134123689357615195>"
    pp = "<:paypal:1134123735499161694>"
    cr = "<:crypto:1134123606209724477>"
    emb = discord.Embed(
        color=0xffffff
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
@commands.is_owner()
async def update(ctx, amount: int=None):
    c = bot.get_channel(1134106690342621234)
    old = c.name
    new = int(old) + amount
    c.edit(name=new)
    ctx.message.add_reaction("<:check:1134161196359106600>")


@bot.command()
@commands.is_owner()
async def role(ctx, mbr: discord.Member):
    role = ctx.guild.get_role(1134133770333733017)
    mbr.add_roles(role)
    ctx.message.add_reaction("<:check:1134161196359106600>")


@bot.command()


bot.run("MTEzMzUxMTI2MTA5MTU0MTAwMg.GRje1C.vO-U0tj2-NBGmflWc6W7gEjZuqkuOKoeLy9Yr0")
