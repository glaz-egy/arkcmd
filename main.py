from discord.ext import commands
import configparser
import discord
import utils
import json
import cogs

class arkBot(commands.Bot):
    def __init__(self, config):
        super().__init__(command_prefix=config.prefix)
        self.botConf = config

    async def on_ready(self):
        print('bot booting')

with open('config.json') as f:
        j = json.load(f)

botConf = utils.botConfig(j['botconfig'])

bot = arkBot(botConf)

if __name__ == '__main__':
    bot.add_cog(cogs.ark(bot, botConf, utils.rconConfig(j['server'])))
    bot.add_cog(cogs.Control(bot))
    bot.run(botConf.bottoken)
