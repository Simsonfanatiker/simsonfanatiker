# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

biberapi = ""
ebbyapi = ""
wolfapi = ""
feliapi = ""
lucaapi = ""
einhornapi = "" 
thofelapi = "" 
shepapi = "https://images.dog.ceo/breeds/australian-shepherd/pepper.jpg"

BaseCog = getattr(commands, "Cog", object)


class Animal(BaseCog):
    """commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.biberapi = biberapi
        self.ebbyapi = ebbyapi
        self.wolfapi = wolfapi
        self.shepapi = shepapi
        self.feliapi = feliapi
        self.lucaapi = lucaapi
        self.einhornapi = einhornapi
        self.thofelapi = thofelapi

    

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def shep(self, ctx):
        """Shows a Shep"""
        try:
            await ctx.send("https://images.dog.ceo/breeds/australian-shepherd/pepper.jpg")
            await ctx.send(result[0])
        except:
            await ctx.send("https://www.zooplus.de/magazin/wp-content/uploads/2017/03/fotolia_130372984-768x564.jpg")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def einhorn(self, ctx):
        """Shows a Einhorn"""
        try:
            await ctx.send("https://www.herz-stoffe.at/wp-content/uploads/2018/09/mPT53EQSsDXiXAuG4sJ8.jpg")
            await ctx.send(result[0])
        except:
            await ctx.send("https://www.svz.de/img/panorama/crop17237326/7150981196-cv1_1-w1200/23-90133556-23-90133557-1499356083.jpg")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def thofel(self, ctx):
        """Shows a Thofel"""
        try:
            await ctx.send("https://cdn.discordapp.com/attachments/804382059732271175/877846882385289226/20210427125342_1.jpg")
            await ctx.send(result[0])
        except:
            await ctx.send("https://cdn.discordapp.com/attachments/766771339020468284/877846741959995412/unknown.png")
            await ctx.send("https://cdn.discordapp.com/attachments/766771339020468284/877846665359425576/unknown.png")
            await ctx.send("https://cdn.discordapp.com/attachments/766771339020468284/877846463869239366/unknown.png")
            await ctx.send("leider fehlt die thoflische Beklopptheit xD")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def feli(self, ctx):
        """Shows a Feli"""
        try:
            await ctx.send("https://feli-verkuppelt.jimdosite.com/")
            await ctx.send(result[0])
        except:
            await ctx.send("https://giphy.com/gifs/cartoon-visualstupidity-muvprojekt-jYePm4YOperePV7C4R")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def luca(self, ctx):
        """Shows a Luca"""
        try:
            await ctx.send("https://cutt.ly/simsonfanatiker-sachsen")
            await ctx.send(result[0])
        except:
            await ctx.send("https://i.imgur.com/RRoSVWC.png")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def wolf(self, ctx):
        """Shows a Wolf"""
        try:
            await ctx.send("Sorry Ebbylein <3 <3 xD")
            await ctx.send("https://cdn.discordapp.com/attachments/736677411055206491/854457682996363294/zje.png")
            await ctx.send(result[0])
        except:
            await ctx.send("https://www.hna.de/bilder/2019/10/08/13080649/743673574-bild-st40-klein-auheim-fasanerie-wolf-2e9.jpg")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def biber(self, ctx):
        """Shows a biber"""
        try:
            await ctx.send("https://i.pinimg.com/236x/0e/dd/b0/0eddb089046b8eb170ca006a5f41667d.jpg")
            await ctx.send("oder den hier")
            await ctx.send(result[0])
        except:
            await ctx.send("https://www.kindernetz.de/wissen/tierlexikon/1606404262062,steckbrief-biber-102~_v-16x9@2dXL_-77ed5d09bafd4e3cf6a5a0264e5e16ea35f14925.jpg")

    @commands.command()
    @commands.cooldown(1, 0, commands.BucketType.guild)
    async def ebby(self, ctx):
        """Shows a Ebby"""
        try:
            await ctx.send("https://cdn.discordapp.com/attachments/736677411055206491/875051981159399474/grea.png")
            await ctx.send("oder das knuffige ding")
            await ctx.send(result[0])
        except:
            await ctx.send("https://cdn.discordapp.com/attachments/736677411055206491/873281830231617546/Winter_ist_ooooooooooon_the_Road_xD.png")
            
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
