import sys
sys.path.append('../')

from discord.ext import commands
from utils.asyncRcon import rconClient
from utils import *
import discord

async def server_connect(rcon_conf, cmd):
    try:
        print(rcon_conf.addr)
        async with rconClient(rcon_conf.addr, rcon_conf.port, rcon_conf.password) as ser:
            res = await ser.send(cmd)
        return res
    except Exception as e:
        return '接続に失敗しました'

class ark(commands.Cog):
    def __init__(self, bot, botConf, server):
        self.bot = bot
        self.botConf = botConf
        self.server = server
    
    @commands.command()
    async def arkcmd(self, ctx, *args):
        """サーバ用コマンドを遠隔で実行します"""
        if args == ():
            await ctx.send('引数が必要です')
        else:
            res = await server_connect(self.server, ' '.join(args))
            await ctx.send(res)

